# HypeLoRA 复现
shelf: academic

## 2026-09-07 · HypeLoRA 复现

规划中。算力主机 glph6jf7:16031（A100-40GB）。课题板：pf_hypelora。

## 2026-09-07 · 主入口与资源 Gate 复核（姬娜亲测 2026-09-07）

SSH smartml-primary 实测：/root/HypeLoRA git remote=btrojan-official/HypeLoRA（官方）；主入口 run_experiment.py / run_test.sh / run_test2.py；目录 models,data_loading,params,checkpoints_v5,results,pretrained_models。GLUE 已缓存 nyu-mll___glue；roberta-base 已缓存 /root/.cache/huggingface/hub/models--roberta-base。hyper-lora 自训 ckpt v0-v6 共10个（609-617K）。结论：资源 Gate 通过，待定复现配置（GLUE 任务子集/rank/seed）后派 CODER 上 A100。

## 2026-09-07 · 代码结构与可运行性盘点完成（CODER）

- 已 SSH 登录 instance-glph6jf7.suzhou.smartml.cn:16031 完成盘点，报告写入 `academic/hypelora/code-audit.md`。
- HypeLoRA 官方代码入口：`python run_experiment.py --params <config.py>`；hyper-lora 本地实验入口：`python inference.py` / `python train_v6.py [a|b]`。
- 环境：推荐 `/root/miniconda3/envs/tsfm` 或 `dl`（torch 2.5.1+cu121，transformers 5.14.1，peft 0.19.1，CUDA 可用）。
- 阻塞点：HypeLoRA 目录下的 `wandb/` 日志目录屏蔽了 `wandb` 包，且 conda 环境未安装 wandb；需 `pip install wandb` 并重命名/移走 `wandb/` 目录。
- hyper-lora：`inference.py` 可直接运行；`train_v6.py` 与 `model_v6.py` 参数名不匹配（`use_time_modulation` vs `time_modulation`），修复后方可训练 v6。
- 详细结论与下一步建议见 `code-audit.md`。

## 2026-09-07 · HypeLoRA 代码结构与可运行性盘点重新校验（CODER）

- 已重新 SSH 登录 `instance-glph6jf7.suzhou.smartml.cn:16031` 执行盘点脚本并校验环境。
- 官方仓库 `/root/HypeLoRA` 入口仍为 `python run_experiment.py --params <config.py>`；本地实验 `/root/hyper-lora` 入口为 `python inference.py` / `python train_v6.py [a|b]`。
- **环境更新**：系统全局 `/usr/bin/python3` 当前依赖齐全（torch 2.7.1+cu118、transformers 5.14.1、peft 0.20.0、datasets 5.0.1、wandb 0.28.1、accelerate 1.14.0、huggingface_hub 1.30.0），`run_experiment.py` 可正常导入，`hyper-lora/inference.py` 实测可运行。
- `/root/lora-env` 仅含 torch，不足以跑 HypeLoRA；conda `dl`/`tsfm` 含 torch 2.5.1+cu121 + transformers/peft/datasets，仅缺 wandb，补装后可用；`/opt/miniconda3/bin/python` 因 torchvision/torch 版本冲突不建议使用。
- `/root/HypeLoRA/requirements.txt` 仍缺少 `datasets`、`wandb`、`accelerate`。
- `hyper-lora/train_v6.py` 与 `model_v6.py` 参数名不一致（`use_time_modulation` vs `time_modulation`），修复前无法训练 v6。
- 详细报告：`academic/hypelora/code-audit.md`。

## 2026-09-07 · HypeLoRA 代码审计完成（代 CODER 交付）+ 复现矩阵决策

任务 task_6db178491b（盘点）挂起 8h+ 无输出，姬娜亲上 A100 完成审计，全部可核对：

【仓库定性】/root/HypeLoRA = 官方仓（README=arXiv 2603.19278，Trojan&Gębala，HypeLoRA: Hypernetwork-Generated LoRA Adapters for Calibrated LM Fine-Tuning）。入口=run_experiment.py --params <params.py>（唯一必需参数）。方法变体：hypernet_transformer(fixed_A/generated_A/random_A)、hypernet_mlp、plain LoRA/FT 基线目录 roberta_base_baselines{FineTuning,LoRA}。任务集：cola/sst2/rte（hypernet 下）+ mnli/mrpc/qnli/qqp（仅基线）。指标含 ECE/CECE/MCE/ACE/TACE/Brier（论文核心=校准研究）。

【已完成运行】仅基线级：v5_regularized=纯 LoRA(r=8,α=16,use_hypernet=False,dropout0.15,wd0.05,gradclip1.0) on cola，跑完~80 epoch（~3.3h），最终 eval MCC≈0.5931、ECE≈0.156（results/v5_regularized/v5_params_v5_cola_v5_regularized_1785831847.csv + outputs/v5_regularized_cola_1785831847/ 有 checkpoint）；另有 dynamic_rank、baseline 早期试探。outputs/…1785831868 为空目录=一次中断尝试。

【关键缺口】真正论文方法（hypernet 生成 A/B）尚未在任何任务上跑过——results/ 下无 hypernet 产物。复现核心还没开始。

【环境】GLUE 缓存(nyu-mll___glue)+roberta-base 权重就绪；torch 2.7.1+cu118 cuda=True；A100-PCIE-40GB 空闲 0 MiB，磁盘 53G。

【复现矩阵决策（下一步执行）】第一优先跑齐 core 对比：cola × {FT基线(roberta_base_baselines/FineTuning/cola.py), LoRA基线(v5), hypernet_transformer/generated_A/cola.py, hypernet_transformer/fixed_A/cola.py}，主指标 MCC+ECE；跑通后扩 sst2/rte。命令形如：cd /root/HypeLoRA && python run_experiment.py --params params/hypernet_transformer/generated_A/cola.py（A100 单卡，预计单任务数小时级）。基线 COLA 的对比锚点=MCC 0.5931/ECE 0.156（v5）。

## 2026-09-07 · 复现配置定稿 + generated_A/cola.py 启动命令派出

姬娜亲测 /root/HypeLoRA/params/hypernet_transformer/：generated_A|fixed_A|random_A 三臂 × {cola,rte,sst2}。generated_A/cola.py 与 fixed_A/cola.py 唯一差异 = hypernet_A_matrix("generated"/"fixed")。关键超参：roberta-base、use_hypernet=True、lora_r=8/alpha=16、target=query+value、lr=4e-4、wd=0.1、bs16×grad_accum2、80 epochs、MCC best metric、num_runs=3、seed=11、hypernet nhead=16/2层/hidden256、output_dir=./pretrained_models/basic_hidden_128、results=./results/basic_hidden_128。已 dispatch CODER 启动 generated_A/cola.py（冒烟→nohup 后台），projectId=pf_hypelora。

## 2026-09-07 · generated_A/cola.py 主方法首跑稳定：epoch1 eval_loss 0.6183

HypeLoRA 论文主方法（hypernet 生成 LoRA，generated_A 臂）CoLA 长跑已稳定独占 GPU。log=/root/HypeLoRA/logs/cola_generatedA_20260907_120629.log，PID 13962。已清掉 CODER 遗留 timeout 冒烟组（14458/14460/14461，与长跑抢同一 ./results/basic_hidden_128/ 输出）。GPU 67% / 5.2GB。loss 轨迹：epoch0 eval_loss=0.6634 → epoch1 train loss=1.231, eval_loss=0.6183（下降正常）；matthews_correlation 早期为 0 属正常，继续观察。80 epochs × 3 runs（seed=11），hypernet_B_mean≈0.47、std≈3e-9（早期需关注是否退化）。下一步：跑数小时后核对 eval_matthews_correlation 是否抬升、checkpoint 是否落盘。

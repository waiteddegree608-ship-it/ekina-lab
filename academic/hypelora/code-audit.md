# HypeLoRA 代码结构与可运行性盘点

> 盘点主机：`instance-glph6jf7.suzhou.smartml.cn:16031`（root）  
> 盘点日期：2026-09-07（本报告基于当日的远程实测数据重新校验后生成）  
> 盘点人：Ekina CODER（OpenCode Go）

## 1. 目录结构摘要

### `/root/HypeLoRA`（官方仓库）

顶层结构（节选）：

```
drwxr-xr-x 15 root root 4096 Aug  4 16:24 .
drwxr-xr-x  8 root root 4096 Aug  1 01:51 .git
-rw-r--r--  1 root root 10376 Jul 31 02:18 README.md
-rw-r--r--  1 root root    80 Aug  4 16:02 requirements.txt
drwxr-xr-x  2 root root    10 Aug  4 16:02 checkpoints_v5     # 空或近空
drwxr-xr-x  3 root root    91 Jul 31 03:07 data_loading
drwxr-xr-x  3 root root   165 Aug  1 01:42 models
drwxr-xr-x  9 root root   4096 Aug  4 16:06 params
drwxr-xr-x  6 root root   174 Jul 31 11:03 pretrained_models
drwxr-xr-x  9 root root   4096 Aug  4 16:24 results
drwxr-xr-x  8 root root   168 Aug  4 16:24 outputs
drwxr-xr-x  8 root root   168 Aug  4 16:24 wandb
-rw-r--r--  1 root root 13388 Aug  1 02:11 run_experiment.py   # 主入口
-rw-r--r--  1 root root   341 Aug  1 02:11 run_test.sh
-rw-r--r--  1 root root 13019 Aug  4 16:05 train_v5.py
-rw-r--r--  1 root root 12842 Jul 31 02:18 calibration_metrics.py
-rwxr-xr-x  1 root root   494 Aug  1 02:17 run_test2.py
-rw-r--r--  1 root root  2364 Aug  1 02:37 test_dynamic_rank.py
-rw-r--r--  1 root root  1955 Aug  1 02:44 test_dynamic_rank2.py
-rw-r--r--  1 root root   568 Aug  1 03:05 test_full.py
```

主要子目录说明：

| 目录 | 内容 |
|------|------|
| `models/` | `hypernet.py`、`dynamic_lora_layer.py`、`get_roberta.py` |
| `data_loading/` | GLUE 数据加载与 tokenization |
| `utils/` | 训练回调、metrics、数据 collator、scheduler 等 |
| `params/` | `baseline/`、`dynamic_rank/`、`hypernet_mlp/`、`hypernet_transformer/`、`roberta_base_baselines/`、`roberta_large_baselines/`、`v5/` 等配置 |
| `results/` / `outputs/` | 历史运行结果与 checkpoint |
| `pretrained_models/` | 本地保存的预训练模型（当前多为空目录） |

### `/root/hyper-lora`（本地实验代码）

顶层结构（节选）：

```
drwxr-xr-x 3 root root   4096 Aug  4 16:54 .
drwxr-xr-x 2 root root   4096 Aug  4 15:16 __pycache__
-rw-r--r-- 1 root root   2422 Aug  4 14:58 compare_v4_v5.py
-rw-r--r-- 1 root root   4263 Aug  4 15:03 compare_v4_v5_ood.py
-rw-r--r-- 1 root root   4679 Aug  4 15:40 compare_v4_v5_v6_fixed.py
-rw-r--r-- 1 root root   1870 Jul 24 03:25 dataset.py
-rw-r--r-- 1 root root   4550 Jul 24 11:34 dataset_v4.py
-rw-r--r-- 1 root root 623509 Jul 24 02:49 hyperlora_meaningful.pt
-rw-r--r-- 1 root root 623381 Jul 24 02:34 hyperlora_v0.pt
-rw-r--r-- 1 root root 623381 Jul 24 03:11 hyperlora_v2.pt
-rw-r--r-- 1 root root 623381 Jul 24 10:15 hyperlora_v3.pt
-rw-r--r-- 1 root root 623044 Jul 24 11:05 hyperlora_v4_best.pt
-rw-r--r-- 1 root root 623058 Jul 24 11:05 hyperlora_v4_final.pt
-rw-r--r-- 1 root root 631502 Aug  4 14:33 hyperlora_v5_best.pt
-rw-r--r-- 1 root root 631533 Aug  4 14:36 hyperlora_v5_final.pt
-rw-r--r-- 1 root root 631502 Aug  4 15:21 hyperlora_v6_best.pt
-rw-r--r-- 1 root root 631533 Aug  4 15:24 hyperlora_v6_final.pt
-rw-r--r-- 1 root root   1336 Jul 24 02:53 inference.py
-rw-r--r-- 1 root root   1755 Jul 24 11:30 inference_v4.py
-rw-r--r-- 1 root root   1261 Jul 24 02:01 model.py
-rw-r--r-- 1 root root   1437 Aug  4 14:16 model_v5.py
-rw-r--r-- 1 root root   2908 Aug  4 16:50 model_v6.py
-rw-r--r-- 1 root root    840 Jul 24 00:06 test_gpu.py
-rw-r--r-- 1 root root   1688 Jul 24 02:33 train.py
-rw-r--r-- 1 root root   3199 Jul 24 03:06 train_larger.py
-rw-r--r-- 1 root root   2803 Jul 24 02:49 train_meaningful.py
-rw-r--r-- 1 root root   1881 Jul 24 10:12 train_v3.py
-rw-r--r-- 1 root root   1842 Jul 24 10:39 train_v4.py
-rw-r--r-- 1 root root   3321 Aug  4 14:16 train_v5.py
-rw-r--r-- 1 root root   3894 Aug  4 16:54 train_v6.py
-rw-r--r-- 1 root root   3452 Jul 29 03:57 visualize_weights.py
```

## 2. 主代码判定与入口

| 目录 | 是否官方仓库 | 依据 | 主入口 |
|------|--------------|------|--------|
| `/root/HypeLoRA` | **是** | `git remote -v` 指向 `https://github.com/btrojan-official/HypeLoRA.git`，当前分支 `main` @ `aff4460`；有完整 `README.md`、`requirements.txt`、`models/`、`utils/`、`params/` | `python run_experiment.py --params <config.py>` |
| `/root/hyper-lora` | **否** | 无 `.git`、无 `README.md`、无 `requirements.txt`；是个人/实验性小项目 | `python train_v6.py [a\|b]` / `python inference.py` |

### HypeLoRA 入口命令

```bash
cd /root/HypeLoRA
# 基线
python run_experiment.py --params params/roberta_base_baselines/FineTuning/cola.py
python run_experiment.py --params params/roberta_base_baselines/LoRA/cola.py

# 超网络实验
python run_experiment.py --params params/hypernet_mlp/fixed_A/cola.py
python run_experiment.py --params params/hypernet_mlp/gen_A/cola.py
python run_experiment.py --params params/hypernet_transformer/fixed_A/cola.py
```

`run_test.sh` 中已有关闭 WandB 的示例：

```bash
export WANDB_MODE=disabled
python3 run_experiment.py --params params/dynamic_rank/cola_test.py
```

### hyper-lora 入口命令

```bash
cd /root/hyper-lora
# 训练最新版（mode a/b 控制时间调制开关）
python train_v6.py a   # -> hyperlora_v6a_best.pt / final.pt
python train_v6.py b   # -> hyperlora_v6b_best.pt / final.pt

# 推理
python inference.py    # 加载 hyperlora_meaningful.pt
```

## 3. Checkpoint 情况

`/root/hyper-lora` 下所有 `.pt` 文件（无 `.ckpt`）：

| 文件 | 大小 | 说明 |
|------|------|------|
| `hyperlora_meaningful.pt` | 623,509 B (~609 KB) | inference.py 默认加载 |
| `hyperlora_v0.pt` | 623,381 B (~609 KB) | 早期版本 |
| `hyperlora_v2.pt` | 623,381 B (~609 KB) | 早期版本 |
| `hyperlora_v3.pt` | 623,381 B (~609 KB) | 早期版本 |
| `hyperlora_v4_best.pt` | 623,044 B (~609 KB) | v4 best |
| `hyperlora_v4_final.pt` | 623,058 B (~609 KB) | v4 final |
| `hyperlora_v5_best.pt` | 631,502 B (~617 KB) | v5 best |
| `hyperlora_v5_final.pt` | 631,533 B (~617 KB) | v5 final |
| `hyperlora_v6_best.pt` | 631,502 B (~617 KB) | v6 best |
| `hyperlora_v6_final.pt` | 631,533 B (~617 KB) | v6 final |

**格式**：PyTorch `state_dict`（`collections.OrderedDict`）。抽样 `hyperlora_v6_best.pt` 显示 key 如 `encoder.0.weight`（形状 `[32, 3, 3, 3]`）、`encoder.0.bias`（`[32]`）等，属于一个 CNN/MLP 混合的小模型。所有权重文件均在 600 KB 左右，**不是完整的 LLM checkpoint**。

`/root/HypeLoRA/checkpoints_v5` 目录近空，历史结果主要分布在 `outputs/`、`results/`、`pretrained_models/`、`wandb/`。

## 4. 当前环境是否 ready

### 基础环境

- OS：`Linux instance-glph6jf7 5.15.0-56-generic #62-Ubuntu`
- 全局 Python：`3.10.12`（`/usr/bin/python3`）
- CUDA：`torch.version.cuda = 11.8`
- GPU：`torch.cuda.is_available() == True`

### 多 Python 环境一览

| 环境 | 路径 | torch | transformers | peft | datasets | wandb | 备注 |
|------|------|-------|--------------|------|----------|-------|------|
| 系统全局 python3 | `/usr/bin/python3` | 2.7.1+cu118 | 5.14.1 | 0.20.0 | 5.0.1 | 0.28.1 | **可直接跑 HypeLoRA** |
| lora-env venv | `/root/lora-env/bin/python` | 2.7.1+cu118 | ❌ 缺失 | ❌ 缺失 | ❌ 缺失 | ❌ 缺失 | 仅 torch，不足以跑 HypeLoRA |
| conda dl | `/root/miniconda3/envs/dl/bin/python` | 2.5.1+cu121 | 5.14.1 | 0.19.1 | 5.0.0 | ❌ 缺失 | 缺 wandb，补装后可用 |
| conda tsfm | `/root/miniconda3/envs/tsfm/bin/python` | 2.5.1+cu121 | 5.14.1 | 0.19.1 | 5.0.0 | ❌ 缺失 | 缺 wandb，补装后可用 |
| conda base (opt) | `/opt/miniconda3/bin/python` | 2.13.0+cu130 | 5.14.1 | ❌ 导入失败 | — | — | torchvision/torch 版本冲突，不建议使用 |

> 注：`conda info --envs` 在系统 PATH 中不可用，但 `/root/miniconda3` 与 `/opt/miniconda3` 均存在。

### 关键包版本（系统 python3）

| 包 | 版本 | 状态 |
|----|------|------|
| torch | 2.7.1+cu118 | OK |
| transformers | 5.14.1 | OK |
| peft | 0.20.0 | OK |
| datasets | 5.0.1 | OK |
| wandb | 0.28.1 | OK |
| scikit-learn | 1.6.1 | OK |
| numpy | 2.2.6 | OK |
| accelerate | 1.14.0 | OK |
| huggingface_hub | 1.30.0 | OK |

### 依赖文件

- `/root/HypeLoRA/requirements.txt` 仅列出：
  ```
  torch>=2.0.0
  transformers>=4.35.0
  peft>=0.6.0
  scikit-learn>=1.3.0
  numpy>=1.24.0
  ```
  缺少 `datasets`、`wandb`、`accelerate`（README 与代码中均已使用）。
- `/root/hyper-lora` 无 `requirements.txt` / `environment.yml`。

### 实际运行验证

- `HypeLoRA`：`/usr/bin/python3 -c "import run_experiment"` **成功**，`params/example_config_no_hypernet.py` 也能正常加载。
- `hyper-lora`：
  - `/usr/bin/python3 inference.py` **成功**，能加载 `hyperlora_meaningful.pt` 并输出红/蓝图像的 LoRA A/B 矩阵。
  - `train_v6.py` 当前存在参数名不一致：`train_v6.py` 使用 `use_time_modulation=(mode=='b')`，而 `model_v6.py` 的 `__init__` 参数名为 `time_modulation`，直接运行会报错。建议统一参数名后再训练 v6。

## 5. 下一步建议

1. **HypeLoRA 可直接用系统 python3 跑**
   - 当前 `/usr/bin/python3` 依赖齐全，`run_experiment.py` 可正常导入。
   - 建议先做最小 dry-run：
     ```bash
     cd /root/HypeLoRA
     export WANDB_MODE=disabled
     python3 run_experiment.py --params params/example_config_no_hypernet.py
     ```
   - 训练需要联网下载 `roberta-base` 与 GLUE 数据集；若主机无外网，需提前把模型放到 `pretrained_models/`。

2. **补齐 requirements.txt**
   - 在 `/root/HypeLoRA/requirements.txt` 中加入 `datasets`、`wandb`、`accelerate`，并建议给出明确版本，避免再次冲突。

3. **hyper-lora 训练 v6 需先修 bug**
   - 推理脚本 `python3 inference.py` 已验证可用。
   - `train_v6.py` 当前因参数名 `use_time_modulation` 与 `model_v6.py` 的 `time_modulation` 不匹配而崩溃。建议统一参数名（例如把 `train_v6.py` 中的 `use_time_modulation` 改为 `time_modulation`）后再执行 `python3 train_v6.py a` / `python3 train_v6.py b`。
   - 修复前可继续使用 `train_v5.py` 或 `inference.py`。

4. **conda dl/tsfm 环境可选**
   - 这两个环境 torch/transformers/peft/datasets 均可用，仅缺 `wandb`；安装 `pip install wandb` 后即可作为 HypeLoRA 的备选环境。

## 6. 关键路径汇总

| 路径 | 说明 |
|------|------|
| `/root/HypeLoRA` | 官方 HypeLoRA 代码 |
| `/root/HypeLoRA/run_experiment.py` | 官方训练入口 |
| `/root/HypeLoRA/requirements.txt` | 依赖（不完整） |
| `/root/hyper-lora` | 本地实验代码 |
| `/root/hyper-lora/train_v6.py` | 最新训练入口（需修参数名 bug） |
| `/root/hyper-lora/inference.py` | 推理入口 |
| `/root/hyper-lora/hyperlora_v*.pt` | 实验性 checkpoint |

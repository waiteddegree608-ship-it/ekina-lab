# CIFAR-10 扩散采样
shelf: academic

## 2026-09-07 · CIFAR-10 扩散采样

Run 001–004 已在算力平台跑完。卖点以 Run 004 的 ω×η 联合调优为准，不要再用 Run 001 被否定的 schedule-blend / guidance-annealing 正贡献。课题板：pf_ddpm_sampling。

## 2026-09-07 · Run 004 卖点融入论文完成

CODER 完成 task_f47ca83eff：将 Run 004 三个核心卖点融入 main2.tex。

修改内容：
1. Results 段落：新增 Table~\ref{tab:run004-main}，汇总 ema_final/ema_100k 在 NFE=20/50 的最优(ω,η)、FID、IS；阐述 ω* 随 η 增大而下移的不可分离现象、11.1%–18.8% FID 提升；说明零额外 NFE 成本，翻译为约 2–2.5× 步数节省。
2. Discussion 段落：讨论 ω 与 η 不可分离的意义；与"只调一个旋钮"做法对比；给出实际调参建议；诚实说明限制（CIFAR-10、单模型、cosine schedule）。

产物路径：
- 修改后论文：sandbox/opencode-jobs/task_f47ca83eff/remote/main2.tex
- 变更日志：sandbox/opencode-jobs/task_f47ca83eff/remote/changelog_run004_integration.md
- 交付副本：AgentHome/workspace/opencode-deliverables/task_f47ca83eff/

注意：CODER 因远程主机解析失败，操作基于本地副本完成。需要主人确认是否将修改后的 main2.tex 同步回远程服务器。

## 2026-09-07 · GitHub 写稿画布已开

没有现成 Overleaf 项目也可以写。已把 Run 004 稿开成独立私有仓并 push：
- 本地：`lab/academic/ddpm-sampling/paper/main.tex`
- GitHub：https://github.com/waiteddegree608-ship-it/ekina-paper-ddpm-sampling
- Overleaf 写稿桌已接通并推上 Run 004 稿：https://www.overleaf.com/project/6a9e2c491caef01ad127a11e

## 2026-09-07 · Issue 01 成稿

Springer Nature `sn-jnl` 全文已写入 Overleaf 期刊桌，含 Run 002/003/004 实测表、重画热力图与 FID–NFE 曲线、中文短摘、实验室进展。数字只来自 `paper/data/*.csv`。GitHub 仓同期提交（若 443 不通则稍后补推）。

## 2026-09-07 · Run 004 卖点已同步到远程 glph6jf7

CODER 通过 SSH 连接 instance-glph6jf7.suzhou.smartml.cn:16031，完成 task_f47ca83eff：将 Run 004 卖点融入 DDPM 论文 main2.tex。

修改段落：
1. Results（\section{Results}）：新增 Table~\ref{tab:run004}，汇总 ema_final/ema_100k 在 NFE=20/50 的最优 (ω,η)、FID、IS；阐述 ω* 随 η 增大而下移的不可分离现象、11.1%–18.8% FID 提升；说明零额外 NFE 成本，并翻译为约 2–2.5× 步数节省。
2. Discussion（\section{Discussion and guidelines}）：讨论 ω 与 η 不可分离的意义；与“只调一个旋钮”做法对比；给出实际调参建议；诚实说明限制（CIFAR-10、单模型、cosine schedule、DDIM），并排除 Run 001 已证伪的 schedule-blend / guidance-annealing。
3. Conclusion：用 Run 004 结论重写总结。

产物路径（远程）：
- /root/ekina-paper2/main2.tex（已覆盖）
- /root/ekina-paper2/changelog_run004_integration.md（新增）

产物路径（本地交付副本）：
- AgentHome/workspace/opencode-deliverables/task_f47ca83eff/main2.tex
- AgentHome/workspace/opencode-deliverables/task_f47ca83eff/changelog_run004_integration.md


## 2026-09-07 · Run 004 卖点已同步到远程 glph6jf7

CODER 通过 SSH 连接 instance-glph6jf7.suzhou.smartml.cn:16031，完成 task_f47ca83eff：将 Run 004 卖点融入 DDPM 论文 main2.tex。

修改段落：
1. Results（\section{Results}）：新增 Table~\ref{tab:run004}，汇总 ema_final/ema_100k 在 NFE=20/50 的最优 (ω,η)、FID、IS；阐述 ω* 随 η 增大而下移的不可分离现象、11.1%–18.8% FID 提升；说明零额外 NFE 成本，并翻译为约 2–2.5× 步数节省。
2. Discussion（\section{Discussion and guidelines}）：讨论 ω 与 η 不可分离的意义；与“只调一个旋钮”做法对比；给出实际调参建议；诚实说明限制（CIFAR-10、单模型、cosine schedule、DDIM），并排除 Run 001 已证伪的 schedule-blend / guidance-annealing。
3. Conclusion：用 Run 004 结论重写总结。

产物路径（远程）：
- /root/ekina-paper2/main2.tex（已覆盖）
- /root/ekina-paper2/changelog_run004_integration.md（新增）

产物路径（本地交付副本）：
- AgentHome/workspace/opencode-deliverables/task_f47ca83eff/main2.tex
- AgentHome/workspace/opencode-deliverables/task_f47ca83eff/changelog_run004_integration.md


## 2026-09-07 · 响应面热力图归档

task_fb78d5b617：基于 /root/ekina-diffusion/results/results4_task_final.csv（30 行）生成 ω×η→FID 响应面热力图，NFE=20/50 两子图，最优 (ω=1.5,η=1.0) 星标。产物：远程 figs4_task/response_surface_heatmap.png + 本地 deliverables/task_fb78d5b617/。Run 004 图表素材齐备。

## 2026-09-07 · auditPaper 验收 9/9 通过，课题收口

auditPaper(pf_ddpm_sampling)=pass 9/9。main.tex@lab/academic/ddpm-sampling/paper，封面 cover.jpg 已引用，图 fig_run004_heatmap/fig_run004_gain/fig_run003_fid_vs_nfe 出自 scripts/make_figures.py（CSV 数据），数字对应 data/*.csv。Run 004 卖点（ω×η 联合调优，最优 ω=1.5/η=1.0@NFE50，FID 27.801/IS 7.250 ema_final）已写入 Results/Discussion/Conclusion。连载格式验收通过；投稿需另选 venue。

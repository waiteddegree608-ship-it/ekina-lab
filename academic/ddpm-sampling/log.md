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


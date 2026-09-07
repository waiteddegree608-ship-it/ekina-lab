# ddpm 连载推送 · 额度恢复后一键执行单

> 用途：OpenCode 额度（401）恢复后，按此单直接执行，无需再重新思考。
> 状态：稿件 audit 全绿；远端 Overleaf 写稿桌在线（6a9e2c49）；唯一阻塞 = 本地 CLAW 通道额度。

## 当前事实（2026-09-08 上午核）
- 稿件：IEEE Access 格式完整稿，82 行 manuscript，2 页 PDF 曾本地编译验证（143KB）。
- 数据链：Gate CSV → comparison/Δ 表 → 英文稿 + 中文摘要，全部来自实测，无捏造。
- Gate 结论：rho100 相对 rho50 差距 head +2.6 / mid +5.8 / tail +16.2 FID。
- 自适应 CFG 消融最佳：ω0=1.5, γ=0.15 → tail 81.279→72.387（−8.89），all-FID 49.367→46.554（−2.81）。
- 远端：GitHub ekina-lab 与 Overleaf 均配好 token，项目在线。

## 恢复后三步执行
1. **git 核实（只读）**：lab repo 的 `git status`（确认 ddpm 改动未提交）、`git remote -v`、当前分支。
   - 验收：改动清单只含 ddpm-sampling 预期文件；无意外删除。
2. **commit + push GitHub**：单条 commit（message 写清 Gate+消融数字），push 到 ekina-lab。
3. **syncOverleaf**：推送 ddpm paper 目录到远端写稿桌 6a9e2c49。

## 验收标准
- Overleaf 构建成功（主人侧可看到 PDF）。
- 官方 auditPaper 盖章 pass=true。
- 两项都过 → ddpm 板面 blocked → done，收口。

## 注意事项
- 401 时禁止反复重试烧额度；直接报主人充值。
- 数字只许来自 `paper/data/*.csv`，commit 前抽核一次。
- Run 001 已否定的结论（schedule-blend / guidance-annealing）不得混入。
- 本机无 pdflatex/tectonic，编译验证靠 Overleaf 侧；zip 对 Overleaf 有效。

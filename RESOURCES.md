# 软件设计 Resources

## Knowledge

- [书（中文全译）: _软件设计的哲学_ — John Ousterhout](https://cactus-proj.github.io/A-Philosophy-of-Software-Design-zh/)
  本课程的主线教材，21 章 + 总结。第 N 章对应 [[lessons/]] 里的 L N。术语以中文译本为准，含糊处回英文原书核对。
- [作者官方书页（Ousterhout, Stanford）](https://web.stanford.edu/~ouster/cgi-bin/book.php)
  版本差异、勘误、第二版新增章（"Decide What Matters"）与对 Clean Code 的回应。**用 for**：确认某条原则是不是作者本人的原话、以及第二版是否改过。
- [Parnas 1972, "On the Criteria To Be Used in Decomposing Systems into Modules" (PDF)](https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf)
  信息隐藏的原始论文，第 5 章的整章地基。**用 for**：想知道「信息隐藏」到底比「按流程图拆模块」强在哪，读这 15 页就够。
- [Parnas 1972, ACM DL 版本](https://dl.acm.org/doi/10.1145/361598.361623)
  同上，正式出版版本（部分网络环境 403，优先用上面的 PDF）。
- [cppreference — 标准库与内存模型](https://en.cppreference.com/w/)
  本书全部例子已翻成 C/C++；查 `std::vector` 的摊还复杂度、`std::string_view`、`mmap` 语义时用。**用 for**：别让「设计上的简化」被「对标准库的错误假设」拖下水。
- [The Rust Programming Language — API Guidelines 摘要](https://rust-lang.github.io/api-guidelines/)
  Rust 社区的接口设计共识。**用 for**：给「深模块」找一个同语言的第二意见——它会告诉你哪些接口约定是社区默认的，因而可以被「隐藏」进常识。

## Wisdom (Communities)

- [software-design-book Google Group](https://groups.google.com/g/software-design-book)
  作者本人读并回复的邮件列表（前言里明确邀请）。**用 for**：你的真实代码案例是否符合某条原则——作者会直接答。发帖前把代码缩减到一屏。
- [Stanford CS 190 课程](https://web.stanford.edu/~ouster/cgi-bin/book.php)
  书中原则的来源课程：学生写代码 → 大量 code review → 按原则返工。**用 for**：想自己复刻「写-评审-改」的循环。
- [r/cpp 的 design 讨论 & r/rust 的 api-design 标签](https://www.reddit.com/r/rust/)
  英文社区里最接近「设计评审」的日常场所。**用 for**：看真实项目维护者如何用这些词争论，学评审语气。

## Gaps

- 缺少**中文**的高质量代码评审社区。上面几个都在英文语境。
- 缺少「本书原则 vs 你所在代码库现状」的对照案例。这条只能靠你把真实代码片段带进课里来补。
- 缺少系统级/并发场景的专门材料（第 20 章只给了原则）。若之后要做性能专题，需要另找：Systems Performance (Gregg)、Rust 的 `crossbeam` 文档、Linux 的 per-CPU 计数器实践。

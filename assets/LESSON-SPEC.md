# 课程写作规范（第 6–21 章统一标准）

所有 lesson 都是**单个自包含 HTML**，只链接两个共享资源：

```html
<link rel="stylesheet" href="../assets/course.css">
...
<script src="../assets/course.js"></script>   <!-- body 末尾，</main> 之后 -->
```

不要内联 `<style>`，不要引入任何外部字体/JS/CDN。

## 读者画像（硬约束，必须照做）

- **语言：C / C++ / Rust，偏底层或性能敏感。** 原书的 Java 例子要**翻译成 C++ / Rust / C**（可以用 `struct`、`std::vector`、`FILE*`、`read()`、`&mut self`、`Result<T,E>`、裸指针、`unsafe`、`Vec<u8>`、页缓存、mmap、io_uring 之类）。不要再出现 Java 语法。
- 读者的三个真实痛点，每课至少正面回应一个：
  1. **改一个需求要动好几处，怕漏**（变更放大）
  2. **代码评审说不出所以然，只会说「不太好」**（要给可命名的危险信号 red flag + 一句能贴到 MR 评论里的原话）
  3. **模块/类拆得不对，越拆越乱**（深模块 / 信息隐藏 / 边界判断）
- 中文写作，术语用中文译本措辞并括注英文，如「深模块（deep module）」。

## 厚度（比 L1–L5 更厚）

每课 **20 分钟以上**阅读量，**至少 2500 汉字**正文；没有上限——摘译和案例该多长就多长，宁可厚也不删（现有 11 课在 4000 以上，L13 最厚 5870）。必须包含：

1. **至少 2 个 `.excerpt` 原文摘译块**——从 `aposd-src/chNN.zh.md` 里摘 2–5 句原意，用 `\`\`\`` 包裹（见下），行尾或用 `<cite>` 标明来源段落主题。**必须是书里真有的意思**，不许编。机翻味道重的句子要改写通顺，但不能改变论断。
2. **至少 1 个 `.anti` 反例分析块**——左边「这样写」，右边「为什么烂 / 怎么改」，配 C++/Rust 代码。
3. 正文里的代码一律用 `<pre><code>`，短片段用 `<code>`。
4. 结尾给出**一句能贴进 code review 的话**（放在 `.key` 里或单独一段）。

## 组件（只用这些 class，已全部在 course.css 里）

| 用途 | 写法 |
|---|---|
| 引文 | `<blockquote><p>…</p><cite>第 N 章</cite></blockquote>` |
| 原文摘译 | `<div class="excerpt"><span class="src">第 N 章 · 小节主题</span><p>…</p></div>` |
| 反例 | `<div class="anti"><h4>反例</h4><div class="pair"><div><b>这样写</b><pre><code>…</code></pre></div><div><b>为什么烂</b><p>…</p></div></div><p>改法：…</p></div>` |
| 核心结论 | `<div class="key"><p><strong>…</strong></p></div>` |
| 补充卡 | `<div class="card"><h4>标题</h4><p>…</p></div>` |
| 两栏 | `<div class="grid2">…</div>` |
| 三矩形（深度示意） | 见 `lessons/0004-modules-should-be-deep.html`，可复用 |
| 单选 | `<div class="quiz"><p class="q">题干</p><button data-ok="1" data-why="…">A</button><button data-why="…">B</button><button data-why="…">C</button><p class="feedback"></p></div>` |
| 回忆卡 | `<div class="recall"><p>题</p><textarea placeholder="…"></textarea><button class="reveal">对照答案</button><div class="answer">…</div></div>` |
| 场景判断（多行） | `<div class="triage"><p class="score"></p><div class="row"><p>场景</p><div class="opts"><button data-ok="1">标签</button><button>标签</button></div><p class="note">解释</p></div>…</div>` |

**测验铁律**：同一题内每个选项字数尽量相等；正确答案位置要变化，不能总在第一个；不能靠格式或顺序泄露答案。

## 固定骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>L6 · 通用模块更深入 — 软件设计的哲学</title>
<link rel="stylesheet" href="../assets/course.css">
</head>
<body>
<main class="page">

<p class="crumb"><a href="../reference/glossary.html">术语表</a> · 第 6 章 · 课程 6 / 21</p>

<h1>通用模块更深入</h1>
<p class="standfirst">一句话说清这一章的赌注。</p>

<h2><span class="num">6.1</span>小节标题</h2>
…

<hr>

<h2><span class="num">练习</span>…</h2>
<div class="triage">…</div>   <!-- 或 quiz / recall -->

<div class="foot">
  <h4>一手资源</h4>
  <p><a href="https://cactus-proj.github.io/A-Philosophy-of-Software-Design-zh/ch06.html">第 6 章 通用模块更深入（中文全译）</a> — 补一句为什么值得读原文。</p>

  <h4>随时问我</h4>
  <p class="ask">给一个具体到可以直接动手的邀请（贴一段真实代码 / 一个纠结的设计选择）。</p>

  <div class="nav-links">
    <span><a href="0005-information-hiding.html">← L5 · 信息隐藏</a></span>
    <span><a href="0007-different-layers.html">L7 · 不同的层 →</a></span>
  </div>
</div>

</main>
<script src="../assets/course.js"></script>
</body>
</html>
```

小节编号用章号（`<span class="num">6.1</span>`）。

## 原文本地位置

- `aposd-src/chNN.zh.md` — 仅中文，已按标题分好（首选，读它）
- `aposd-src/chNN.cn.txt` — 中英混排全文（zh.md 某句不通时回来对照）
- 第 21 章：`aposd-src/ch21.zh.md`；全书原则小结：`aposd-src/summary.zh.md`

## 自检（交付前必须做）

1. `python3 -c "from html.parser import HTMLParser; ..."` 或至少用 `python3 -c` + `html.parser` 跑一遍，确认标签配对无异常。
2. 所有相对链接（`../assets/course.css`、`../reference/glossary.html`、前后课）指向的文件真实存在。
3. 没有 `<style>`、没有外链 CDN、没有 Java 例子。
4. 每课至少 2 个 `.excerpt`、至少 1 个 `.anti`、至少 1 个交互组件。

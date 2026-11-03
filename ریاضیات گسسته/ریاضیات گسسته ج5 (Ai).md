tags:
  - ریاضیات_گسسته
  - منطق_ریاضی
  - سورها
date: 2026-10-18
---

# سورها و منطق گزاره‌ها

## ۱. جابه‌جایی سورها
> [!important] قانون جابه‌جایی
> در گزاره‌هایی که چند سور مختلف در آن‌ها وجود دارد، **مجاز به جابه‌جایی سورها نیستیم** (جابه‌جایی ممکن است ارزش گزاره را تغییر دهد).

پیوند: [[سور یعنی چی؟]]
### مثال (بررسی ارزش در دامنه $\mathbb{R}$):
1. **گزاره:**
$\forall x \, \exists y \, (x + y = 0)$
   - **ارزش:** $\text{True}$ (درست)
   - *توضیح:* به ازای هر عدد حقیقی $x$، همیشه می‌توان $y = -x$ را پیدا کرد که جمعشان صفر شود.

1. **گزاره:**
$\exists y \, \forall x \, (x + y = 0)$  
   - **ارزش:** $\text{False}$ (نادرست)
   - *توضیح:* یک عدد ثابت $y$ وجود ندارد که با *تمام* مقادیر $x$ جمع شود و حاصل صفر شود.

---

## ۲. قوانین نقیض گزاره‌های سوری
برای نقیض کردن، سورها جابه‌جا می‌شوند ($\forall \to \exists$ و $\exists \to \forall$) و گزاره‌ی درون آن‌ها نیز نقیض می‌شود:

$$
\begin{aligned}
\sim(\forall x \, P(x)) &\equiv \exists x \, \sim P(x) \\
\sim(\exists x \, P(x)) &\equiv \forall x \, \sim P(x) \\
\sim(\forall x \, \forall y \, \sim P(x,y)) &\equiv \exists x \, \exists y \, P(x,y) \\
\sim(\exists x \, \exists y \, P(x,y)) &\equiv \forall x \, \forall y \, \sim P(x,y) \\
\sim(\forall x \, \exists y \, P(x,y)) &\equiv \exists x \, \forall y \, \sim P(x,y) \\
\sim(\exists x \, \forall y \, P(x,y)) &\equiv \forall x \, \exists y \, \sim P(x,y)
\end{aligned}
$$

> [!note] نقیضِ نقیض
> $\sim(\sim(\forall x \, \forall y \, \exists z \, (xz = y))) \equiv \forall x \, \forall y \, \exists z \, (xz = y)$

توضیحات بیشتر: [[قوانین نقیض و گزاره های سوری]]
پیوند: [[منظور از P چیست؟]]

---

## ۳. تمرین‌های نقیض گزاره‌ها

### تمرین ۱:
نقیض گزاره‌ی زیر را به دست آورید:
$$\exists x \, (x < 0 \land q(x))$$

**حل:**
طبق قوانین دمورگان و نقیض سور وجودی:
$$\sim (\exists x \, (x < 0 \land q(x))) \equiv \forall x \, (x \ge 0 \, \lor \sim q(x))$$
*(دقت: نقیضِ $x < 0$ برابر است با $x \ge 0$)*

پیوند: [[قوانین دمورگان]]

---

### تمرین ۲:
نقیض گزاره‌ی زیر را بنویسید:
$$P: \forall x \, \exists y \, \exists z \, \forall q \, \exists r \, (x + y + q + r = 0)$$

**حل:**
$$\sim P \equiv \exists x \, \forall y \, \forall z \, \exists q \, \forall r \, (x + y + q + r \neq 0)$$

---

## ۴. هم‌ارزی شرطی و ساده‌سازی

> [!tip] فرمول هم‌ارزی گزاره شرطی
> $$p \implies q \equiv \, \sim p \lor q$$

لینک: [[گزاره های شرطی]]
### مثال:
نقیض گزاره‌ی $(p \land \sim q) \implies \sim r$ را به دست آورید:

$$
\begin{aligned}
\sim \big( (p \land \sim q) \implies \sim r \big) 
&\equiv \sim \big( \sim(p \land \sim q) \lor \sim r \big) \\
&\equiv \sim(\sim(p \land \sim q)) \land \sim(\sim r) \quad \text{(قانون دمورگان)} \\
&\equiv (p \land \sim q) \land r
\end{aligned}
$$

---

## ۵. ترجمه گزاره‌ها به زبان منطق ریاضی و نقیض آن‌ها

**صورت گزاره:**  
> «به ازای هر عدد حقیقی مثبت $x$ و هر عدد حقیقی $y$، عدد طبیعی چون $n$ وجود دارد به‌طوری که $nx > y$»

- **نمادگذاری به زبان منطق:**
  $$\forall x \in \mathbb{R}^+ \, \forall y \in \mathbb{R} \, \exists n \in \mathbb{N} \, (nx > y)$$

- **نقیض گزاره:**
  $$\exists x \in \mathbb{R}^+ \, \exists y \in \mathbb{R} \, \forall n \in \mathbb{N} \, (nx \le y)$$
توضیحات بیشتر: [[ترجمه متن فارسی به متن منطق ج5]]
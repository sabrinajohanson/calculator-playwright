## 🐛 Bugs found during development

| # | Bug | Root cause | Status |
|---|---|---|---|
| [#1](https://github.com/sabrinajohanson/calculator-playwright/issues/1) | AC button not working | `clear()` is a reserved word in JavaScript | ✅ Fixed |
| [#2](https://github.com/sabrinajohanson/calculator-playwright/issues/2) | Chained operations not accumulating | `operator()` was overwriting state instead of accumulating | ✅ Fixed |
| [#3](https://github.com/sabrinajohanson/calculator-playwright/issues/3) | History showing only last two numbers | `history` variable was being overwritten on every click | ✅ Fixed |
| [#4](https://github.com/sabrinajohanson/calculator-playwright/issues/4) | Percent calculating value instead of percentage | `percent()` was always dividing by 100 regardless of context | ✅ Fixed |
| [#5](https://github.com/sabrinajohanson/calculator-playwright/issues/5) | Numbers losing precision after 15 digits | JavaScript IEEE 754 floating point limitation | ✅ Fixed |
| [#6](https://github.com/sabrinajohanson/calculator-playwright/issues/6) | Backspace blocked after pressing equals | Early return when `justCalculated` was true | ✅ Fixed |
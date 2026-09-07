# CHANGELOG

## 2026-09-07 — LIGHT v0.5

- Добавлен `LIGHT_PROPERTIES.md`: полная карта физических свойств света/электромагнитного излучения и их relation-first mapping.
- Добавлен `FULL_LIGHT_RUN.md`: полный проход по кинематике, полям, энергии, импульсу, поляризации, причинности, взаимодействию, границам, квантованию, интерференции и информации.
- Добавлен `experiments/REL-05_dispersion_energy_momentum.py`: дисперсионный тест `omega(k)` и связь с безмассовой кинематикой.
- Добавлен `experiments/REL-06_polarization_helicity.md`: поперечность, поляризация и helicity.
- Добавлен `experiments/REL-07_stress_energy.md`: энергия, импульс и Maxwell stress layer.
- Добавлен `experiments/REL-08_boundaries.md`: reflection/refraction/diffraction boundary layer.
- Добавлен `experiments/REL-09_matter_interaction.md`: coupling, absorption, emission and scattering.
- Добавлен `experiments/REL-10_quantum_modes.md`: quantum modes, occupation and photon layer.
- Добавлен `experiments/REL-11_interference_coherence_information.md`: interference, coherence and information layer.
- REL-05 подтверждён численно на длинных волнах; дискретизационная дисперсия появляется у Nyquist и не должна интерпретироваться как физическое свойство фотона.
- Добавлена строгая граница: часть слоёв пока архитектурно совместима, но не выведена из Ω аксиом.

## 2026-09-07 — LIGHT v0.4

- Добавлен `experiments/REL-03_gauge_relation_test.py`: дискретный U(1) gauge/connection тест.
- Добавлен `experiments/REL-03.md`: зафиксированы connection, covariant relation, curvature и gauge-invariant energy.
- Зафиксировано H5d: relation-first архитектура совместима с дискретным U(1) gauge/connection слоем на проверенном численном уровне.
- Зафиксирована строгая граница: U(1) пока является входом из установленной QED, а не результатом вывода Ω.
- Следующий риск: проверить, можно ли получить общий паттерн `state → transformation → connection → accumulated relation → invariant` без ручного ввода электромагнитной U(1).

## 2026-09-07 — LIGHT v0.3

- Добавлен `ENERGY_RELATION.md`: энергия включена в relation-first проверку как отдельный количественный критерий.
- Добавлен `experiments/REL-01E_energy_test.py`: скалярная relation-модель + энергетический баланс.
- Добавлен `experiments/REL-01E.md`: зафиксирован результат REL-01E.
- Добавлен `experiments/REL-02E_maxwell_energy_test.py`: минимальная 1D поперечная Maxwell-модель с векторной структурой и энергией.
- Добавлен `experiments/REL-02E.md`: результаты REL-02E и границы интерпретации.
- Зафиксировано H5c: relation-first архитектура сохраняет векторную структуру, распространение и количественный энергетический баланс на проверенном численном уровне.
- Зафиксировано ограничение: REL-02E не является выводом всей электродинамики из абстрактных отношений; gauge/connection, источники, полная 3D-структура и квантовый слой остаются отдельными проверками.

## 2026-09-07 — LIGHT v0.2

- Добавлен QFT_CORE: поле → квантование → фотон.
- Добавлен GAUGE_STRUCTURE: локальная U(1), A_mu, D_mu и F_muν.
- Добавлен LAGRANGIAN: Maxwell/QED и структурная декомпозиция.
- Добавлен MINIMAL_STRUCTURE: поиск минимального структурного скелета.
- Добавлен DERIVATION_CHAIN: последовательность от симметрии к фотону и наблюдению.
- Добавлен LIGHT_HYPOTHESES: гипотезы и критерии фальсификации.
- Зафиксировано ключевое различие: математическая связь/аналогия не считается физическим фактом без отдельной проверки.

## 2026-09-07 — LIGHT v0.1

- Создан фундаментальный каркас исследования света.
- Зафиксированы FIELD, PHOTON, PROPAGATION, INTERACTION, GEOMETRY.
- Добавлен слой Ω_MAPPING с запретом выдавать аналогии за физические факты.
- Добавлен экспериментальный план E0–E5.
- Зафиксировано правило разделения факта, модели, гипотезы и теста.

Следующий этап: полный проход по физическим свойствам света и их relation-first проверке.

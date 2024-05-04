У тестах порівняли час виконання трьох алгоритмів сортування: злиттям, вставками та Timsort (вбудований алгоритм сортування в Python). Ось результати вимірювань:
1. Для списку з 100 елементів:
    * Час сортування злиттям: 0.00018 секунд
    * Час сортування вставками: 0.00021 секунд
    * Час Timsort: 1.4142e-05 секунд
2. Для списку з 1000 елементів:
    * Час сортування злиттям: 0.00465 секунди
    * Час сортування вставками: 0.00463 секунди
    * Час Timsort: 0.000144 секунди
3. Для списку з 10000 елементів:
    * Час сортування злиттям: 0.0316 секунд
    * Час сортування вставками: 3.22234 секунд
    * Час Timsort: 0.00177 секунд
На основі цих даних можна зробити такі висновки:
* Найшвидшим алгоритмом є Timsort, що показує найменший час сортування у всіх тестових випробуваннях. Це пов'язано з тим, що Timsort використовує оптимізації та комбінує різні алгоритми, що робить його ефективним для широкого спектру випадків сортування.
* Часова складність:
    * Вставкове сортування має часову складність O(n^2), де n - кількість елементів у списку. Це означає, що час виконання збільшується квадратично зі збільшенням кількості елементів.
    * Злиттям сортування також має часову складність O(n log n), що робить його більш ефективним порівняно з вставковим сортуванням для великих списків, але менш ефективним ніж Timsort.
    * Timsort, використовуваний в Python, має в середньому часову складність O(n log n), але у певних випадках він може виконуватися швидше, оскільки використовує оптимізації для вже відсортованих частин списку.
Отже, для швидкого сортування списків рекомендується використовувати вбудований алгоритм сортування Timsort, який є ефективним і відповідає багатьом вимогам для різних розмірів списків.
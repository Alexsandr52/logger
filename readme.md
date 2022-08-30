<h3>Логгер</h3>
Разработайте класс Logger, который:
<ul>
    <li>1. Создаёт файл лога при инициализации объекта (по указанному пути или по умолчанию в корневой
папке).
<em>*Обеспечить существование только одного объекта этого класса (паттерн Singleton)</em></li>
<li>2. Название файла должно иметь формат log_dd.mm.yy.</li>
<li>3. Внутри должен быть приватный метод, который возвращает текущую дату.</li>
<li>4. Все события одного дня должны писаться в один файл. Если день меняется, должен создаваться новый
файл при записи в лог по шаблону из п.2</li>
<li>5. Поддерживает метод <strong>write_log()</strong>, записывающий событие в правильный файл дня в формате:
[06:23:15] Произошедшее событие</li>
<li>6. Поддерживает метод <strong>clear_log()</strong>, который удаляет записи в файле текущего дня.</li>
<li>7. Поддерживает метод <strong>get_logs()</strong>, возвращающий записи из файла текущего дня в виде списка (один
элемент списка — запись одного события).</li>
<li>8. Поддерживает метод <strong>get_last_event()</strong>, который возвращает запись о последнем событии.</li>
<li>9. Поддерживает метод <strong>get_all_logs()</strong>, который возвращает список всех файлов лога.</li>
Предусмотреть крайние ситуации при которых возможен вылет. Исключить возможные ошибки
конструкциями <strong>try-except</strong> и <strong>raise exception</strong>.
</ul>
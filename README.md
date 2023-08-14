<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <h1>Riot ELO Bot</h1>
    <p>Riot ELO Bot - это бот на платформе Telegram, разработанный с использованием библиотеки <code>telebot</code>. Бот запрашивает Riot ID у пользователя, выполняет запрос к серверу для получения количества ELO игрока и предоставляет информацию о результатах.</p>
    <h2>Особенности</h2>
    <ul>
        <li>Запрос Riot ID у пользователя.</li>
        <li>Выполнение запроса к серверу для получения информации о количестве ELO игрока.</li>
        <li>Отправка информации о количестве ELO обратно пользователю в чат.</li>
    </ul>
    <h2>Использование</h2>
    <ol>
        <li>Запустите бот, предоставив свой токен Телеграмм бота.</li>
        <li>Пользователь вводит команду <code>/start</code>, и бот просит ввести Riot ID.</li>
        <li>После ввода Riot ID, бот запрашивает Riot Tag.</li>
        <li>После ввода Riot Tag, бот выполняет запрос к серверу Valorant для получения количества ELO игрока.</li>
        <li>Бот отправляет информацию о количестве ELO игрока обратно в чат.</li>
    </ol>
    <h2>Установка</h2>
    <ol>
        <li>Клонируйте репозиторий:</li>
        <pre><code>https://github.com/IcodedthiswhenIwasdrunk/valorantpalyeelofinder.git</code></pre>
        <li>Установите зависимости:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li>Вставьте свой токен Telegram в settings.py:</li>
        <pre><code>TOKEN = 'YOUR_BOT_TOKEN'</code></pre>
        <li>Укажите свой регион Valorant в settings.py:</li>
        <pre><code>valorant_region = 'your_region'</code></pre>
        <li>Запустите бота:</li>
        <pre><code>python main.py</code></pre>
    </ol>
    <h2>Зависимости</h2>
    <ul>
        <li><code>telebot</code>: Библиотека для работы с API Telegram.</li>
        <li><code>requests</code>: Библиотека для выполнения HTTP-запросов.</li>
    </ul>
</body>
</html>

@echo off
chcp 65001 > nul
echo === Тест 2: Запуск с VFS и скриптом 2 ===
python conf1.py conf1.py script2.sh c2.toml

echo.
echo === Тестирование завершено ===
pause

@echo off
chcp 65001 > nul
echo === Тест 1: Запуск с VFS и скриптом 1 ===
python conf1.py conf1.py script1.sh c1.toml

echo.
echo === Тестирование завершено ===
pause

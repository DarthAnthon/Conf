@echo off
chcp 65001 > nul
echo === Тест 0: Запуск с VFS и скриптом 0 ===
python conf1.py conf1.py start_script.sh configuration_file.toml

echo.
echo === Тестирование завершено ===
pause

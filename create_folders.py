import json
import os
from pathlib import Path

def create_controller_folders(input_file='merged_updated.json', base_folder='controllers'):
    """
    Создаёт папки с названиями контроллеров из JSON файла
    """
    
    # Читаем файл
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Раскладываем вложенные списки (на всякий случай)
    flat_data = []
    for item in data:
        if isinstance(item, list):
            flat_data.extend(item)
        else:
            flat_data.append(item)
    
    # Извлекаем названия контроллеров
    controllers = []
    for item in flat_data:
        if isinstance(item, dict):
            # Очищаем ключ от пробелов
            name = item.get('name', item.get('name ', '')).strip()
            if name:
                controllers.append(name)
    
    # Удаляем дубликаты и сортируем
    controllers = sorted(list(set(controllers)))
    
    # Создаём базовую папку
    Path(base_folder).mkdir(exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"ВСЕГО КОНТРОЛЛЕРОВ: {len(controllers)}")
    print(f"{'='*60}\n")
    
    # Создаём папки
    created = 0
    skipped = 0
    
    for name in controllers:
        folder_path = Path(base_folder) / name
        
        # Заменяем недопустимые символы в имени папки
        safe_name = name.replace('/', '-').replace('\\', '-').replace(':', '-').replace('*', '-').replace('?', '-').replace('"', '-').replace('<', '-').replace('>', '-').replace('|', '-')
        folder_path = Path(base_folder) / safe_name
        
        if folder_path.exists():
            print(f"⊘ Пропущено: {safe_name} (уже существует)")
            skipped += 1
        else:
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Создано: {safe_name}")
            created += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Готово! Создано папок: {created}, Пропущено: {skipped}")
    print(f"📁 Папки находятся в: {os.path.abspath(base_folder)}")
    print(f"{'='*60}\n")
    
    return controllers

if __name__ == '__main__':
    create_controller_folders()
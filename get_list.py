import json

def extract_controller_list(input_file='merged_updated.json', output_file='controllers_list.txt'):
    """
    Извлекает список всех контроллеров из JSON файла
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
    
    # Извлекаем названия
    controllers = []
    for item in flat_data:
        if isinstance(item, dict):
            # Очищаем ключ от пробелов
            name = item.get('name', item.get('name ', '')).strip()
            if name:
                controllers.append(name)
    
    # Сортируем по алфавиту
    controllers.sort()
    
    # Вывод в консоль
    print(f"\n{'='*60}")
    print(f"ВСЕГО КОНТРОЛЛЕРОВ: {len(controllers)}")
    print(f"{'='*60}\n")
    
    for i, name in enumerate(controllers, 1):
        print(f"{i:3}. {name}")
    
    # Сохраняем в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Список контроллеров Onbon ({len(controllers)} шт.)\n")
        f.write("="*60 + "\n\n")
        for i, name in enumerate(controllers, 1):
            f.write(f"{i}. {name}\n")
    
    print(f"\n✅ Список сохранён в {output_file}")
    return controllers

if __name__ == '__main__':
    extract_controller_list()
import json

def flatten_and_add_fields(input_file='merged.json', output_file='merged_updated.json'):
    """
    1. Раскладывает вложенные списки в один плоский список
    2. Очищает ключи от пробелов
    3. Добавляет 3 новых поля
    """
    
    # Читаем файл
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # 1. Раскладываем вложенные списки (flatten)
    flat_data = []
    for item in raw_data:
        if isinstance(item, list):
            flat_data.extend(item)  # Добавляем элементы внутреннего списка
        else:
            flat_data.append(item)  # Добавляем сам объект
    
    print(f"Загружено и расложено {len(flat_data)} контроллеров")
    
    # 2. Обрабатываем каждый контроллер
    for i, controller in enumerate(flat_data):
        if not isinstance(controller, dict):
            continue
            
        # Очищаем ключи от пробелов (например "name " -> "name")
        controller = {k.strip(): v for k, v in controller.items()}
        
        # Очищаем ключи внутри specs, если есть
        if 'specs' in controller and isinstance(controller['specs'], dict):
            controller['specs'] = {k.strip(): v for k, v in controller['specs'].items()}
        
        # 3. Добавляем новые поля
        controller['additional_info'] = ''      # 1. Дополнительная информация
        controller['manual_url'] = ''           # 2. Ссылка на спецификацию/мануал
        controller['photo_url'] = ''            # 3. Ссылка на фото
        
        flat_data[i] = controller
        
        if (i + 1) % 10 == 0:
            print(f"Обработано {i + 1}/{len(flat_data)}")
    
    # Сохраняем результат
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(flat_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Готово! Файл сохранён как {output_file}")
    return flat_data

if __name__ == '__main__':
    flatten_and_add_fields()
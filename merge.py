import json
import os
from pathlib import Path

def merge_json_files(folder_path='.', output_file='merged.json'):
    """
    Объединяет все JSON-файлы из папки в один массив объектов.
    """
    merged_data = []
    json_files = list(Path(folder_path).glob('*.json'))
    
    print(f"Найдено файлов: {len(json_files)}")
    
    for file_path in json_files:
        # Пропускаем выходной файл, если он уже существует
        if file_path.name == output_file:
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                merged_data.append(data)
                print(f"✓ Добавлен: {file_path.name}")
        except Exception as e:
            print(f"✗ Ошибка в файле {file_path.name}: {e}")
    
    # Сохраняем результат
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Готово! {len(merged_data)} объектов сохранено в {output_file}")
    return merged_data

# Запуск
if __name__ == '__main__':
    merge_json_files()
# import pytest
# from unittest.mock import patch, MagicMock
# import pandas as pd
# from your_module import reader_file_transactions_xlxs  # Замените your_module на имя вашего модуля
#
#
# @pytest.fixture
# def mock_pd_read_excel():
#     with patch('pandas.read_excel') as mock:
#         yield mock
#
#
# # Тест на успешное чтение Excel файла
# def test_reader_file_transactions_xlxs_success(mock_pd_read_excel):
#     # Подготовка тестовых данных
#     test_data = [
#         {"id": "1", "date": "2023-01-01", "amount": "100", "description": "Payment"},
#         {"id": "2", "date": "2023-01-02", "amount": "200", "description": "Transfer"},
#     ]
#
#     # Создаем mock DataFrame
#     mock_df = MagicMock()
#     mock_df.to_dict.return_value = test_data
#
#     # Настраиваем mock для pd.read_excel
#     mock_pd_read_excel.return_value = mock_df
#
#     # Вызываем функцию
#     result = reader_file_transactions_xlxs("dummy_path.xlsx")
#
#     # Проверяем результаты
#     assert result == test_data
#     mock_pd_read_excel.assert_called_once_with(
#         "dummy_path.xlsx",
#         dtype=str,
#         engine="openpyxl"
#     )
#     mock_df.to_dict.assert_called_once_with(orient="records")
#
#
# # Тест на случай, когда файл не найден
# def test_reader_file_transactions_xlxs_file_not_found(mock_pd_read_excel):
#     mock_pd_read_excel.side_effect = FileNotFoundError("File not found")
#
#     result = reader_file_transactions_xlxs("nonexistent_file.xlsx")
#
#     assert result == []
#     mock_pd_read_excel.assert_called_once()
#
#
# # Тест на случай, когда произошла другая ошибка
# def test_reader_file_transactions_xlxs_general_exception(mock_pd_read_excel):
#     mock_pd_read_excel.side_effect = Exception("Some error")
#
#     result = reader_file_transactions_xlxs("corrupted_file.xlsx")
#
#     assert result == []
#     mock_pd_read_excel.assert_called_once()
#
#
# # Тест на случай, когда Excel файл пустой
# def test_reader_file_transactions_xlxs_empty_file(mock_pd_read_excel):
#     mock_df = MagicMock()
#     mock_df.to_dict.return_value = []
#
#     mock_pd_read_excel.return_value = mock_df
#
#     result = reader_file_transactions_xlxs("empty_file.xlsx")
#
#     assert result == []
#     mock_pd_read_excel.assert_called_once()
#     mock_df.to_dict.assert_called_once_with(orient="records")
#
#
# # Тест на случай, когда Excel файл содержит некорректные данные
# def test_reader_file_transactions_xlxs_invalid_data(mock_pd_read_excel):
#     test_data = [
#         {"id": "1", "date": "2023-01-01", "amount": "invalid", "description": "Payment"},
#         {"id": "2", "date": "2023-01-02", "amount": "200", "description": "Transfer"},
#     ]
#
#     mock_df = MagicMock()
#     mock_df.to_dict.return_value = test_data
#
#     mock_pd_read_excel.return_value = mock_df
#
#     result = reader_file_transactions_xlxs("invalid_data.xlsx")
#
#     assert result == test_data
#     mock_pd_read_excel.assert_called_once()
#     mock_df.to_dict.assert_called_once_with(orient="records")

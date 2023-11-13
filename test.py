from Classes import Converter as Converter

converter = Converter.Converter('data/latest.json')

converter.load_latest_data()
converter.load_mapping_data()

print(converter.latest_data_to_dataframe())

# need to change latest data to dataframe
## in converter class, the columns need to be mapped
## the way they are in mapping
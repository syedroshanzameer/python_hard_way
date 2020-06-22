class hadoop(object):
         
    def __init__(self):
        %config PPMagics.autolimit=0
        %hive_stampy SET hive.tez.container.size=10240

    def create_table(database,table,query):
        init_param = hadoop.param()
        %hive_stampy use {database}
        check = %hive_stampy show tables like "{table}"
        if len(check) > 0:
            print('Table with name "{table}" already exists!'.format(table))
        else:
            result = %hive_stampy {query}
            result_df = result.DataFrame()
            %hive_stampy -df result_df -t {database}.{table}
        return result_df
     
    def param():
        %config PPMagics.autolimit=0
        %hive_stampy SET hive.tez.container.size=10240
         
    def query(query):
        init_param = hadoop.param()
        result = %hive_stampy {query}
        return result
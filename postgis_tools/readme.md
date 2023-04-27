## exportar .shp
pgsql2shp -f <filename>.shp -g <columnname> -h <hostname> -u <userdb> -P <passdb> <dbname> <query_with_columnname>
## importar .shp
shp2pgsql -s 4326 -I <filename>.shp <schema>.<new_table> > <sql_file_output>.sql

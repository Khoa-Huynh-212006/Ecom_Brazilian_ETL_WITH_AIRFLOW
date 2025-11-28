to_mysql:
	docker exec -it de_mysql mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}"

to_mysql_root:
	docker exec -it mysql mysql -u"root" -p"${MYSQL_ROOT_PASSWORD}" "${MYSQL_DATABASE}"

mysql_create:
	docker exec -it de_mysql mysql --local_infile -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}" -e "source /tmp/load_dataset/mysql_datasource.sql"
mysql_load:
	docker exec -it mysql_ecom_project mysql --local_infile -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}" -e "source /tmp/load_dataset/mysql_load.sql"

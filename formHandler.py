def queryHandler(provinces, jobs):
    queryHead = "SELECT latitude, longitude, province, employer, address, requested_lmia, LEFT(occupation, 4) AS occ FROM lmia_tb"
    queryTail = []
    if provinces: 
        queryTail.append("province IN (" + ', '.join(f"'{province}'" for province in provinces) + ")")
    if jobs: 
        queryTail.append("occupation IN (" + ', '.join(f"'{job}'" for job in jobs) + ")")

    if queryTail ==[] :
        return f"{queryHead};"
    else:
        return f"{queryHead} WHERE " + "AND ".join(queryTail) + ";"
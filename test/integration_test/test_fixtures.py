# Copyright 2018 eQualit.ie
# See LICENSE for other credits and copying information

# Constants used in the test

class TestFixtures:
    FATAL_ERROR_INDICATOR = "[ABORT]"
    DEFAULT_PROCESS_TIMEOUT = 15 # seconds
    TCP_TRANSPORT_TIMEOUT = 15 
    I2P_TRANSPORT_TIMEOUT = 600
    
    REPO_FOLDER_NAME = "repos"

    INJECTOR_CONF_FILE_NAME = "ouinet-injector.conf"
    INJECTOR_IPNS_PERSISTANT_IDENTITY = { "Identity": {"PeerID": "QmQdMc9wqxhmcwr5iYn4t48EDVUCD96FjyVn7ZdgowkxL2",
                                            "PrivKey": "CAASpwkwggSjAgEAAoIBAQDCW6vOI/6msrbswRy/wKFp/4gbhkYQ9RYFb4Ty4kKVFagK8irkyqINDr8lqBRwqUM52h0zqa0e6Yj3cJ5QEpdmanrVOZ1mVnc3gFibcQc1vIMnJz/mI14CH17NOFaxLRONGAV/98u2JsnGIHsJ+JGzpxGSyHDv5k2geaRNOYa4NUn/ry3x6gZL2G6XBMWHzgUeMvmNyZ7BKKWaVONn+QbAdJgrI32rD5q9cKptbLBiLj70a0Jxgt6zNCfnhLvRKhSW2P9bmqqTPnxYBjTsfpqV8D646n2r5P7mvD8KT5D75aiqP4EkjwyMzI3OppsxDt3EArlcWKN85k6yEFOuM75NAgMBAAECggEABXNouBlOVQKCGtW3prESVdSyzoLPiD43ZeOgyOcLkv7OfbAY/92m+dLGDZpPKHG2zvKNCxvhHRLToozoA7rhwB+QXlaFUY9vPIE++u0KlLk6vGhfZGbthgW3NO41kDaBa92WmeYrMmqYEhRrHvZ3r6Ap4AH7GN9OogeHUhsg6h2X7e+FyWLCd3x9UIhGeY0D4jLrapj7x6CTx9Yw1/KdjEcCWy5zGSr7W+qVi3DsVv0H6bnIEVcfbve8V0C8sA6Lb4JQxr38hzb8EDfsMMTGzGHhDi0He6ftR56p/XBu2wZN/+yr3rAfvHKYuNXEBx80Lv4TAoxrGfqQt/L4RIRZSQKBgQDNgqQnThCUMHAwE+kC22fhiuvl3Nmyx8QPxbTBJu1gGergKCu0m9uNX5hQdN+9/ieCzTakth0oETx3Vz+DzI0FjVC9yr30kiNeaFMToBCEenYcGGCC3U2Vz6ppquiZAvVm025MvLHiAH3n/PS3yXEzoYSHUDNhi/+ddNoP4I+ElwKBgQDyG59Crup1amLXBc/Z0YTcGApnU9dbCTinmdpCRQVQczRj29tVOu05QSk1wQ0d2+V12Ydg2VD97rAx9T0mFFHq0QS7/I9fNCajerR3R0f7wsyrHZovFN8mTEh8fxl8pO3i0ScH7L1Z0wQbuxAzgehqmEoaj7ULkNfU0tgUhNm8uwKBgQCOhyhpyg5deCqWbXiQ7rHhDoQEa2LgRwOHHMr7mo/Osqrew31sSRu/tKjiQ+xYzEeCw+g927/k5e9VpUD7m4XCb/urZUzQrfmxpBDZ740FFBmN6qokmG8Sk2/Q0SN320FvCvvYZJXJ9CVeG2VtgVvtPvu3DLxVzs582WnS0R84CQKBgAnllSoNqmnoUmgFxcxaozq4BNzacYg4JUe8o05oMeJrAy4904Z1ZTMc9clLvfSFg6jAnqcX2xa2Rh+Urc47sGmP58ijd1zl7dpq7qudj1S8Ts+D40SfbsvK/H+SVoFg4JSQBi9tvwPH+3gCupPQcKbC2OyjCTySzC/X+ptEHv53AoGAJy5KhFBEQNTD3M942QJfTVdZL6i5c54hsaszblhcA+4yG2l3QEwad9HjofzfILhCsh8ZZg2o7yODBkgIwGYROX/GxbAhvAsRrHgCEUshV5hM6Ei3dFRyZt+d7AYqjWDs1d38XX0pFbMrSI0P/LlMpiVz64aIiDg6QsnIQL6FTVs="}}

    INJECTOR_I2P_PUBLIC_ID = "tR0ADsik-0Gn4F-t6WICzUT59H9NlUnejCknd4E4XZNha8B0zR8zFW6va~MpCzMdlE7FxChpHM9MjMnuR1PcakaKU9i5E0wJ~cP2oQd1GTCtMARmpsILysN4brfEvU2TAn1n7JZnHpMHSRPaPTqk7g-ReLR8jN5yQBOedxmmKIJspcOhTjRprqceKjoPpmHzqPgVtrspgQAOIUCcRQ3S44DGUfN603Woqlci6XDmMZW4gktHEygCoIbaXMbvt7gCY6S5PI5ENu-3xsKKZG5B7RUzDQGX5iQHfRLe9utGMRQf63RneFuXZ6hfMSSv7TXm7emUpw5gDXFoLK9GT3NDPPmjX3kU-SlNxF2BfI38YU8fuqguZEjQO0w89O8DbyKvqxBTS5scxucIw5Gu3qZX98If20QzVqk2ZaEeA8LTCIWsM4mi9Mmw~fD7fyX9fnmGNFHrDkXbNtZU-8K9TzB4Ka4KHJRBQIlNDKCT3LMKs5PJuW4TYtNb2M8UV2UsIFouBQAEAAEAAA=="

    INJECTOR_I2P_PRIVATE_KEY = "tR0ADsik-0Gn4F-t6WICzUT59H9NlUnejCknd4E4XZNha8B0zR8zFW6va~MpCzMdlE7FxChpHM9MjMnuR1PcakaKU9i5E0wJ~cP2oQd1GTCtMARmpsILysN4brfEvU2TAn1n7JZnHpMHSRPaPTqk7g-ReLR8jN5yQBOedxmmKIJspcOhTjRprqceKjoPpmHzqPgVtrspgQAOIUCcRQ3S44DGUfN603Woqlci6XDmMZW4gktHEygCoIbaXMbvt7gCY6S5PI5ENu-3xsKKZG5B7RUzDQGX5iQHfRLe9utGMRQf63RneFuXZ6hfMSSv7TXm7emUpw5gDXFoLK9GT3NDPPmjX3kU-SlNxF2BfI38YU8fuqguZEjQO0w89O8DbyKvqxBTS5scxucIw5Gu3qZX98If20QzVqk2ZaEeA8LTCIWsM4mi9Mmw~fD7fyX9fnmGNFHrDkXbNtZU-8K9TzB4Ka4KHJRBQIlNDKCT3LMKs5PJuW4TYtNb2M8UV2UsIFouBQAEAAEAAE7cmUpeDXDkMEy3Br08viGl5MDBvVe9DGRiGyg-WzIm8uQ0054Q2APSmljEDN21JFMnrvbYn1BgCzCOXKJjd4T9C7Ms~NR0XJGSUMiIiclKHBYNkP~SoFiBX2PD3CThfq56t7HikE9EtO1K9rLEh5uwoxqyyBdbqxEN6yzDZOX5znajTr~6rwZ0EebaNBG9cb76UAA69gc-9HfpYE0py~yb6qcfQuXoQy0m8gVMffJymNw-sXbNJMzb8qHAeH8i24LRleLU-MrvqmAw7RM1Tg3AlK4e3d0I3acgnGsPmqdir01F5Sbb3ETpmIU6sfngbs9pGwZ7ZKio2r1hzlZX7EkvaLJhUhGZJWwzxqHDhhX6llDF168OsJHlOoeqPU35Ug=="

    I2P_TUNNEL_READY_REGEX = r'[\s\S]*I2P Tunnel has been established'
    INJECTOR_PORT = 7070
    INJECTOR_CONF_FILE_CONTENT = "open-file-limit = 32768\n"
    
    TEST_PAGE_BODY="<html><body>TESTPAGE</body></html>\n"
    TEST_HTTP_SERVER_PORT = 7080
    RESPONSE_LENGTH = 20

    CLIENT_CONFIG_FILE_NAME = "ouinet-client.conf"
    FIRST_CLIENT = { "name": "client1",
                         "port": 8081}

    FIRST_CLIENT_CONF_FILE_CONTENT = "open-file-limit = 4096\n"

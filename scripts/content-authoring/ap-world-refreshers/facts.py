"""Date check for the World History content (refreshers, questions and free-response prompts). Every time an event is named with
a year right after it ("Treaty of Versailles (1919)", "the Black Death in 1347"), the year must be one of the dates in this
table. It only catches a date that disagrees with the table, so the table itself is the thing to verify (standard, well-documented
dates). Run from this folder: python3 facts.py"""
import glob, json, re

EVENTS = {
 r"Song dynasty": {960, 1279}, r"Abbasid caliphate": {750, 1258}, r"Kamakura shogunate": {1185, 1192}, r"Baghdad": {762, 1258},
 r"Ain Jalut": {1260}, r"Delhi Sultanate": {1206, 1526}, r"Vijayanagara": {1336}, r"Majapahit": {1293}, r"Mansa Musa": {1324, 1325},
 r"Magna Carta": {1215}, r"Black Death": {1347, 1351, 1348, 1346}, r"Crusades?": {1095, 1291, 1096}, r"Yuan dynasty": {1271, 1368},
 r"Genghis Khan": {1206, 1227}, r"Ming dynasty": {1368, 1644}, r"Zheng He": {1405, 1433, 1431}, r"Constantinople": {1453},
 r"Safavid": {1501, 1722}, r"Mughal Empire": {1526, 1857}, r"Qing dynasty": {1644, 1912}, r"Tokugawa": {1603, 1868}, r"Chaldiran": {1514},
 r"Thirty Years' War": {1618, 1648}, r"Peace of Westphalia": {1648}, r"Martin Luther": {1517}, r"Dias": {1488}, r"da Gama": {1498},
 r"Columbus": {1492}, r"Magellan": {1519, 1522}, r"Dutch East India Company|VOC": {1602}, r"English East India Company": {1600},
 r"Malacca": {1511}, r"Newton": {1687}, r"Wealth of Nations": {1776}, r"Wollstonecraft": {1792}, r"Haitian Revolution": {1791, 1804},
 r"American Revolution": {1775, 1783}, r"French Revolution": {1789, 1799}, r"Reign of Terror": {1793, 1794}, r"Napoleon": {1799, 1804, 1815, 1769, 1821},
 r"Communist Manifesto": {1848}, r"Tanzimat": {1839, 1876}, r"Self-Strengthening": {1861, 1895}, r"Meiji": {1868, 1912},
 r"Berlin Conference": {1884, 1885}, r"Opium Wars?": {1839, 1842, 1856, 1860}, r"Taiping": {1850, 1864}, r"Boxer": {1899, 1901, 1900},
 r"Adwa": {1896}, r"Maji Maji": {1905, 1907}, r"Indian National Congress": {1885}, r"Suez Canal": {1869, 1956}, r"Panama Canal": {1914},
 r"Chinese Exclusion Act": {1882}, r"White Australia": {1901}, r"Franz Ferdinand": {1914}, r"Brest-Litovsk": {1918}, r"Treaty of Versailles": {1919},
 r"Armenian genocide": {1915}, r"Russian Revolution": {1917}, r"Salt March": {1930}, r"Munich": {1938}, r"Anschluss": {1938}, r"Rhineland": {1936},
 r"Nazi-Soviet Pact": {1939}, r"Stalingrad": {1942, 1943}, r"D-Day": {1944}, r"Nanjing": {1937, 1938}, r"Nuremberg": {1945, 1946},
 r"United Nations": {1945}, r"Genocide Convention": {1948}, r"Iron Curtain": {1946}, r"Truman Doctrine": {1947}, r"Marshall Plan": {1948},
 r"Berlin Airlift|Berlin blockade": {1948, 1949}, r"NATO": {1949}, r"Warsaw Pact": {1955}, r"Korean War": {1950, 1953}, r"Cuban Missile Crisis": {1962},
 r"Berlin Wall": {1961, 1989}, r"Sputnik": {1957}, r"Bandung": {1955}, r"Dien Bien Phu": {1954}, r"Algerian War": {1954, 1962}, r"Great Leap Forward": {1958, 1962},
 r"Cultural Revolution": {1966, 1976}, r"Solidarity": {1980}, r"Tiananmen": {1989}, r"Universal Declaration of Human Rights": {1948},
 r"Montreal Protocol": {1987}, r"Rio Earth Summit": {1992}, r"Kyoto Protocol": {1997}, r"Paris Agreement": {2015}, r"Bretton Woods": {1944},
 r"WTO|World Trade Organization": {1995, 2001}, r"NAFTA": {1993, 1994}, r"Maastricht": {1992}, r"OPEC": {1960, 1973}, r"Chernobyl": {1986},
 r"Rwanda": {1994}, r"Hiroshima": {1945}, r"Pearl Harbor": {1941}, r"Gorbachev": {1985, 1991}, r"Ghana": {1957}, r"Mau Mau": {1952, 1960},
}
AFTER = re.compile(r"^(?:\s*[,(]?\s*(?:of|in|from|during)?\s*\(?(?P<y>\d{4})s?\b)")
bad = 0
for path in sorted(glob.glob("../../../content/ap-world/**/*.json", recursive=True)):
    if "/units/" in path or path.endswith("course.json"):
        continue
    data = json.load(open(path))
    strings = []
    def walk(x, where):
        if isinstance(x, str):
            strings.append((where, x))
        elif isinstance(x, list):
            for i in x: walk(i, where)
        elif isinstance(x, dict):
            for k, v in x.items(): walk(v, where + "." + k)
    for item in data:
        walk(item, item.get("id") or f'{item["unit"]}/{item["topic"]}')
    for where, text in strings:
        for pat, ok in EVENTS.items():
            for m in re.finditer(pat, text):
                a = AFTER.match(text[m.end():m.end() + 24])
                if a:
                    y = int(a.group("y"))
                    if y not in ok:
                        bad += 1
                        print(f"{where}: '{m.group(0)}' followed by {y}, expected {sorted(ok)} :: ...{text[max(0, m.start() - 30):m.end() + 40]!r}")
print("flags:", bad)

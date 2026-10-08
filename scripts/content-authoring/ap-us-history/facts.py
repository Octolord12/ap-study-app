"""Date check for the APUSH content: every time an event is named with a year right after it ("the Stamp Act of 1765",
"Fort Mose in 1738", "Dominion of New England (1686)"), the year must be one of the dates in this table. It only catches
a date that disagrees with the table, so the table itself is the thing to verify (it is written from standard,
well-documented dates)."""
import glob, json, re, sys

EVENTS = {
 r"Tordesillas": {1494}, r"Reformation": {1517}, r"Armada": {1588}, r"Roanoke": {1585, 1587, 1590}, r"St\. Augustine": {1565},
 r"Potos\S*": {1545}, r"Columbus": {1492}, r"Reconquista": {1492}, r"Cortes|Cort\S*s": {1519, 1521},
 r"Jamestown": {1607}, r"Mayflower": {1620}, r"Massachusetts Bay": {1630}, r"Pennsylvania": {1681, 1682, 1780, 1838},
 r"Georgia": {1732}, r"Navigation Acts?": {1651, 1660, 1663}, r"Dominion of New England": {1686}, r"Bacon's Rebellion": {1676},
 r"Stono": {1739}, r"Pueblo Revolt": {1680}, r"King Philip's War": {1675, 1676}, r"Zenger": {1735}, r"Salem witch trials?": {1692},
 r"Half-Way Covenant": {1662}, r"Glorious Revolution": {1688, 1689}, r"Fort Mose": {1738}, r"Yamasee War": {1715},
 r"New Netherland": {1624, 1664}, r"French and Indian War": {1754, 1763}, r"Proclamation of 1763": {1763}, r"Stamp Act": {1765, 1766},
 r"Declaratory Act": {1766}, r"Townshend": {1767}, r"Boston Massacre": {1770}, r"Boston Tea Party": {1773}, r"Coercive Acts?": {1774},
 r"Common Sense": {1776}, r"Saratoga": {1777}, r"Yorktown": {1781}, r"Treaty of Paris": {1763, 1783, 1898}, r"Northwest Ordinance": {1787},
 r"Shays' Rebellion": {1786, 1787}, r"Bill of Rights": {1791}, r"Whiskey Rebellion": {1794}, r"Jay's Treaty": {1795}, r"Pinckney's Treaty": {1795},
 r"Greenville": {1795}, r"Fallen Timbers": {1794}, r"XYZ Affair": {1797, 1798}, r"Alien and Sedition Acts": {1798}, r"Virginia and Kentucky Resolutions": {1798, 1799},
 r"Farewell Address|farewell address": {1796}, r"Proclamation of Neutrality": {1793}, r"Dunmore": {1775}, r"Vermont": {1777}, r"Marbury v\. Madison": {1803},
 r"Louisiana Purchase": {1803}, r"Embargo Act": {1807}, r"Hartford Convention": {1814, 1815}, r"McCulloch v\. Maryland": {1819}, r"Missouri Compromise": {1820},
 r"Monroe Doctrine": {1823}, r"Erie Canal": {1825}, r"cotton gin": {1793}, r"Indian Removal Act": {1830}, r"Worcester v\. Georgia": {1832}, r"Trail of Tears": {1838, 1839},
 r"Nullification Crisis": {1832, 1833}, r"The Liberator": {1831}, r"Nat Turner": {1831}, r"Seneca Falls": {1848}, r"Panic of 1837": {1837}, r"Specie Circular": {1836},
 r"gag rule": {1836, 1844}, r"Annexation of Texas|annexation of Texas": {1845}, r"Mexican-American War": {1846, 1848}, r"Guadalupe Hidalgo": {1848}, r"Oregon Treaty": {1846},
 r"Gold Rush": {1848, 1849}, r"Compromise of 1850": {1850}, r"Kansas-Nebraska Act": {1854}, r"Dred Scott": {1857}, r"Emancipation Proclamation": {1863}, r"Gettysburg": {1863},
 r"Vicksburg": {1863}, r"Antietam": {1862}, r"Appomattox": {1865}, r"Thirteenth Amendment": {1865}, r"Fourteenth Amendment": {1868}, r"Fifteenth Amendment": {1870},
 r"Compromise of 1877": {1877}, r"Panic of 1873": {1873}, r"Freeport Doctrine": {1858}, r"Harpers Ferry": {1859}, r"Uncle Tom's Cabin": {1852},
 r"Enforcement Acts": {1870, 1871}, r"Civil Rights Act of 1866": {1866}, r"Reconstruction Acts": {1867}, r"Slaughterhouse Cases": {1873},
 r"transcontinental railroad": {1869}, r"Sherman Antitrust Act": {1890}, r"Interstate Commerce Act": {1887}, r"Haymarket": {1886}, r"Homestead Strike": {1892}, r"Pullman": {1894},
 r"Dawes Act": {1887}, r"Wounded Knee": {1890}, r"Pendleton": {1883}, r"Plessy v\. Ferguson": {1896}, r"Civil Rights Cases": {1883}, r"Atlanta Compromise": {1895},
 r"Chinese Exclusion Act": {1882}, r"Ellis Island": {1892}, r"Hull House": {1889}, r"Omaha Platform": {1892}, r"Exodusters": {1879}, r"Homestead Act": {1862}, r"Munn v\. Illinois": {1877},
 r"Spanish-American War": {1898}, r"Open Door notes": {1899, 1900}, r"Platt Amendment": {1901}, r"Roosevelt Corollary": {1904}, r"The Jungle": {1906}, r"Zimmermann Telegram": {1917},
 r"Schenck v\. United States": {1919}, r"Fourteen Points": {1918}, r"Treaty of Versailles": {1919}, r"Scopes Trial": {1925}, r"Immigration Act of 1924": {1924}, r"Social Security Act": {1935},
 r"Wagner Act|National Labor Relations Act": {1935}, r"Pearl Harbor": {1941}, r"Lend-Lease Act": {1941}, r"Executive Order 8802": {1941}, r"Executive Order 9066": {1942}, r"Korematsu": {1944},
 r"NAACP": {1909}, r"Seventeenth Amendment": {1913}, r"Federal Reserve Act": {1913}, r"GI Bill": {1944}, r"Taft-Hartley Act": {1947}, r"Marshall Plan": {1948},
 r"Federal-Aid Highway Act": {1956}, r"Brown v\. Board of Education": {1954}, r"Montgomery Bus Boycott": {1955, 1956}, r"Civil Rights Act of 1964": {1964}, r"Voting Rights Act of 1965": {1965},
 r"Gulf of Tonkin Resolution": {1964}, r"Cuban Missile Crisis": {1962}, r"Immigration and Nationality Act": {1965}, r"Title IX": {1972}, r"Silent Spring": {1962}, r"Stonewall": {1969},
 r"Pentagon Papers": {1971}, r"Engel v\. Vitale": {1962}, r"Little Rock": {1957}, r"Gideon v\. Wainwright": {1963}, r"Miranda v\. Arizona": {1966}, r"Roe v\. Wade": {1973},
 r"PATCO|air traffic controllers": {1981}, r"Berlin Wall": {1989}, r"Gulf War": {1991}, r"NAFTA": {1993, 1994}, r"Personal Responsibility and Work Opportunity Act": {1996},
 r"Patriot Act": {2001}, r"Dodd-Frank Act": {2010}, r"Obergefell v\. Hodges": {2015}, r"Lawrence v\. Texas": {2003}, r"Deferred Action for Childhood Arrivals": {2012},
 r"Immigration Reform and Control Act": {1986}, r"Proposition 187": {1994}, r"Contract with America": {1994}, r"Arab Spring": {2011}, r"Strategic Defense Initiative": {1983},
 r"INF Treaty": {1987}, r"Troubled Asset Relief Program": {2008}, r"Iran-Contra": {1986, 1987},
}
AFTER = re.compile(r"^(?:\s*[,(]?\s*(?:of|in|from|during)?\s*\(?(?P<y>\d{4})s?\b)")
bad = 0
for path in sorted(glob.glob("../../../content/ap-us-history/**/*.json", recursive=True)):
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

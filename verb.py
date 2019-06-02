import re
import sys
from parse import get_forms,wword,cur,form_exists,esc

energ = """\<center\>\ \Ε\ξ\α\κ\ο\λ\ο\υ\θ\η\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\ \<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Ε\ν\ε\σ\τ\ώ\τ\α\ς
\<\/th\>
\<th\>\Π\α\ρ\α\τ\α\τ\ι\κ\ό\ς
\<\/th\>
\<th\>\Ε\ξ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Μ\ε\τ\ο\χ\ή
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<EX_MEL_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<YPOT_EX_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<METOXI>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_G_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_A_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_B_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_PL>.*?)
\<\/td\>
\<td\>\θ\α (.*?)
\<\/td\>
\<td\>\ν\α (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_G_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>\<center\>\ \Σ\υ\ν\ο\π\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\ \<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>
\<\/th\>
\<th\>\Α\ό\ρ\ι\σ\τ\ο\ς
\<\/th\>
\<th\>\Σ\υ\ν\ο\π\τ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Α\π\α\ρ\έ\μ\φ\α\τ\ο
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\ rowspan\=\"6\"\>
\<\/td\>
\<td\>(?P<AOR_A_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<AOR_APAREMFATO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<AOR_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PROST_AOR_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<AOR_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_G_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_PL>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_B_PL>.*?)\
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_PL>.*?)
\<\/td\>
\<td\>(?P<PROST_AOR_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<AOR_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_G_PL>.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
"""
b = """\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>\<center\>\ \Σ\υ\ν\τ\ε\λ\ε\σ\μ\έ\ν\ο\ι\ \χ\ρ\ό\ν\ο\ι\ \<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Π\α\ρ\α\κ\ε\ί\μ\ε\ν\ο\ς
\<\/th\>
\<th\>\Υ\π\ε\ρ\σ\υ\ν\τ\έ\λ\ι\κ\ο\ς
\<\/th\>
\<th\>\Σ\υ\ν\τ\ε\λ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>\έ\χ\ω\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\α\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ω\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ω\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>\έ\χ\ε\ι\ς\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\ε\ς\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\ι\ς\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\ι\ς\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\έ\χ\ε\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>\έ\χ\ε\ι\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\ι\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\ι\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>\έ\χ\ο\υ\μ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\α\μ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ο\υ\μ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ο\υ\μ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>\έ\χ\ε\τ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\α\τ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\τ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\τ\ε\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\έ\χ\ε\τ\ε\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>\έ\χ\ο\υ\ν\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ε\ί\χ\α\ν\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\θ\α\ \έ\χ\ο\υ\ν\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>\ν\α\ \έ\χ\ο\υ\ν\ \α\λ\λ\ά\ξ\ε\ι
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>\<center\>\ \Σ\υ\ν\τ\ε\λ\ε\σ\μ\έ\ν\ο\ι\ \χ\ρ\ό\ν\ο\ι\ \β\΄\ \(\μ\ε\τ\α\β\α\τ\ι\κ\ο\ί\)\<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Π\α\ρ\α\κ\ε\ί\μ\ε\ν\ο\ς
\<\/td\>
\<td\ colspan\=\"6\"\>\έ\χ\ω\ \(\έ\χ\ε\ι\ς\,\ \έ\χ\ε\ι\,\ \έ\χ\ο\υ\μ\ε\,\ \έ\χ\ε\τ\ε\,\ \έ\χ\ο\υ\ν\)\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ε\ρ\σ\υ\ν\τ\έ\λ\ι\κ\ο\ς
\<\/td\>
\<td\ colspan\=\"6\"\>\ε\ί\χ\α\ \(\ε\ί\χ\ε\ς\,\ \ε\ί\χ\ε\ \,\ \ε\ί\χ\α\μ\ε\,\ \ε\ί\χ\α\τ\ε\,\ \ε\ί\χ\α\ν\)\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Σ\υ\ν\τ\ε\λ\.\ \Μ\έ\λ\λ\.
\<\/td\>
\<td\ colspan\=\"6\"\>\θ\α\ \έ\χ\ω\ \(\θ\α\ \έ\χ\ε\ι\ς\,\ \θ\α\ \έ\χ\ε\ι\,\ \θ\α\ \έ\χ\ο\υ\μ\ε\,\ \θ\α\ \έ\χ\ε\τ\ε\,\ \θ\α\ \έ\χ\ο\υ\ν\)\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/td\>
\<td\ colspan\=\"6\"\>\ν\α\ \έ\χ\ω\ \(\ν\α\ \έ\χ\ε\ι\ς\,\ \ν\α\ \έ\χ\ε\ι\,\ \ν\α\ \έ\χ\ο\υ\μ\ε\,\ \ν\α\ \έ\χ\ε\τ\ε\,\ \ν\α\ \έ\χ\ο\υ\ν\)\ \α\λ\λ\α\γ\μ\έ\ν\ο
\<\/td\>\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>\<center\>\ \Σ\υ\ν\τ\ε\λ\ε\σ\μ\έ\ν\ο\ι\ \χ\ρ\ό\ν\ο\ι\ \β\΄\ \(\α\μ\ε\τ\ά\β\α\τ\ο\ι\)\<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Π\α\ρ\α\κ\ε\ί\μ\ε\ν\ο\ς
\<\/td\>
\<td\ colspan\=\"6\"\>\<a\ href\=\"https\:\/\/el\.wiktionary\.org\/wiki\/\%CE\%B5\%CE\%AF\%CE\%BC\%CE\%B1\%CE\%B9\"\ title\=\"\ε\ί\μ\α\ι\"\>\ε\ί\μ\α\ι\<\/a\>\,\ \ε\ί\σ\α\ι\,\ \ε\ί\ν\α\ι\ \<a\ href\=\"https\:\/\/el\.wiktionary\.org\/wiki\/\%CE\%B1\%CE\%BB\%CE\%BB\%CE\%B1\%CE\%B3\%CE\%BC\%CE\%AD\%CE\%BD\%CE\%BF\%CF\%82\"\ title\=\"\α\λ\λ\α\γ\μ\έ\ν\ο\ς\"\>\α\λ\λ\α\γ\μ\έ\ν\ο\ς\<\/a\>\ \-\ \ε\ί\μ\α\σ\τ\ε\,\ \ε\ί\σ\τ\ε\,\ \ε\ί\ν\α\ι\ \α\λ\λ\α\γ\μ\έ\ν\ο\ι
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ε\ρ\σ\υ\ν\τ\έ\λ\ι\κ\ο\ς
\<\/td\>
\<td\ colspan\=\"6\"\>\ή\μ\ο\υ\ν\,\ \ή\σ\ο\υ\ν\,\ \ή\τ\α\ν\ \α\λ\λ\α\γ\μ\έ\ν\ο\ς\ \-\ \ή\μ\α\σ\τ\ε\,\ \ή\σ\α\σ\τ\ε\,\ \ή\τ\α\ν\ \α\λ\λ\α\γ\μ\έ\ν\ο\ι
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Σ\υ\ν\τ\ε\λ\.\ \Μ\έ\λ\λ\.
\<\/td\>
\<td\ colspan\=\"6\"\>\θ\α\ \ε\ί\μ\α\ι\,\ \θ\α\ \ε\ί\σ\α\ι\,\ \θ\α\ \ε\ί\ν\α\ι\ \α\λ\λ\α\γ\μ\έ\ν\ο\ς\ \-\ \θ\α\ \ε\ί\μ\α\σ\τ\ε\,\ \θ\α\ \ε\ί\σ\τ\ε\,\ \θ\α\ \ε\ί\ν\α\ι\ \α\λ\λ\α\γ\μ\έ\ν\ο\ι
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/td\>
\<td\ colspan\=\"6\"\>\ν\α\ \ε\ί\μ\α\ι\,\ \ν\α\ \ε\ί\σ\α\ι\,\ \ν\α\ \ε\ί\ν\α\ι\ \α\λ\λ\α\γ\μ\έ\ν\ο\ς\ \-\ \ν\α\ \ε\ί\μ\α\σ\τ\ε\,\ \ν\α\ \ε\ί\σ\τ\ε\,\ \ν\α\ \ε\ί\ν\α\ι\ \α\λ\λ\α\γ\μ\έ\ν\ο\ι
\<\/td\>\<\/tr\>\<\/tbody\>"""
verb = """\<center\>\Ε\ξ\α\κ\ο\λ\ο\υ\θ\η\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\<\/center\>
\<\/th\>\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Ε\ν\ε\σ\τ\ώ\τ\α\ς
\<\/th\>
\<th\>\Π\α\ρ\α\τ\α\τ\ι\κ\ό\ς
\<\/th\>
\<th\>\Ε\ξ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Μ\ε\τ\ο\χ\ή
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_A_ENIKO>.*?)
\<\/td\>
""""""\<td\>(?P<PARATATIKOS_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<EX_MEL_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<YPOT_EX_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<METOXI>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_ENIKO>.*?)
<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_G_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_A_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_B_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_PL>.*?)
\<\/td\>
\<td\>\θ\α(.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_G_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_PL>.*?)
<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>"""
"""\<center\>\Σ\υ\ν\ο\π\τ\ι\κ\ο\ί\ \χ\ρ\ό\ν\ο\ι\<\/center\>
\<\/th\>
\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α\<\/th\>
\<th\>\<\/th\>
\<th\>\Α\ό\ρ\ι\σ\τ\ο\ς\<\/th\>
\<th\>\Σ\υ\ν\ο\π\τ\.\ \Μ\έ\λ\λ\.\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή\<\/th\>
\<th\ align\=\"center\"\>\Α\π\α\ρ\έ\μ\φ\α\τ\ο\<\/th\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\ rowspan\=\"6\"\>\<\/td\>
\<td\>(?P<AOR_A_ENIKO>.*?)\<\/td\>
\<td\>\θ\α\ (.+?)\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_ENIKO>.*?)\<\/td\>
\<td\>\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"(?P<AOR_APAREMFATO>.*?)\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\>(?P<AOR_B_ENIKO>.*?)\<\/td\>
\<td\>\θ\α\ (.+?)\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_ENIKO>.*?)\<\/td\>
\<td\>(?P<PROST_AOR_B_ENIKO>.*?)<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\>(?P<AOR_G_ENIKO>.*?)\<\/td\>
\<td\>\θ\α\ (.*?)\<\/td\>
\<td\>\ν\α(?P<AOR_YPOT_G_ENIKO>.*?)\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.\<\/td\>
\<td\>(?P<AOR_A_PL>.*?)\<\/td\>
\<td\>\θ\α\ (.*?)\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_A_PL>.*?)\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.\<\/td\>
\<td\>(?P<AOR_B_PL>.*?)\<\/td\>
\<td\>\θ\α\ (.*?)\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_B_PL>.*?)\<\/td\>
\<td\>(?P<PROST_AOR_B_PL>.*?)\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.\<\/td\>
\<td\>(?P<AOR_G_PL>.*?)\<\/td\>
\<td\>\θ\α\ (.*?)\<\/td\>
\<td\>\ν\α\ (?P<AOR_YPOT_G_PL>.*?)\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>
\<center\>\Σ\υ\ν\τ\ε\λ\ε\σ\μ\έ\ν\ο\ι\ \χ\ρ\ό\ν\ο\ι\<\/center\>
\<\/th\>
\<\/tr\>
\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α\<\/th\>
\<th\>\Π\α\ρ\α\κ\ε\ί\μ\ε\ν\ο\ς\<\/th\>
\<th\>\Υ\π\ε\ρ\σ\υ\ν\τ\έ\λ\ι\κ\ο\ς\<\/th\>
\<th\>\Σ\υ\ν\τ\ε\λ\.\ \Μ\έ\λ\λ\.\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή\<\/th\>
\<th\>\<\/th\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\>\έ\χ\ω\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\α\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ω\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ω\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\<\/td\>
\<td\ rowspan\=\"6\"\>\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\>\έ\χ\ε\ι\ς\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\ε\ς\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\ι\ς\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\ι\ς\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\έ\χ\ε\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.\<\/td\>
\<td\>\έ\χ\ε\ι\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\ι\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\ι\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.\<\/td\>
\<td\>\έ\χ\ο\υ\μ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\α\μ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ο\υ\μ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ο\υ\μ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.\<\/td\>
\<td\>\έ\χ\ε\τ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\α\τ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ε\τ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ε\τ\ε\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\έ\χ\ε\τ\ε\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.\<\/td\>
\<td\>\έ\χ\ο\υ\ν\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ε\ί\χ\α\ν\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\θ\α\ \έ\χ\ο\υ\ν\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\ν\α\ \έ\χ\ο\υ\ν\ \λ\ύ\σ\ε\ι\<\/td\>
\<td\>\<\/td\>
\<\/tr\>
\<tr\>
\<th\ colspan\=\"7\"\ style\=\"background\:\#e2e4c0\"\>
\<center\>\Σ\υ\ν\τ\ε\λ\ε\σ\μ\έ\ν\ο\ι\ \χ\ρ\ό\ν\ο\ι\ \β\΄\ \(\μ\ε\τ\α\β\α\τ\ι\κ\ο\ί\)\<\/center\>
\<\/th\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Π\α\ρ\α\κ\ε\ί\μ\ε\ν\ο\ς\<\/td\>
\<td\ colspan\=\"6\"\>\έ\χ\ω\ \(\έ\χ\ε\ι\ς\,\ \έ\χ\ε\ι\,\ \έ\χ\ο\υ\μ\ε\,\ \έ\χ\ε\τ\ε\,\ \έ\χ\ο\υ\ν\)\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ε\ρ\σ\υ\ν\τ\έ\λ\ι\κ\ο\ς\<\/td\>
\<td\ colspan\=\"6\"\>\ε\ί\χ\α\ \(\ε\ί\χ\ε\ς\,\ \ε\ί\χ\ε\ \,\ \ε\ί\χ\α\μ\ε\,\ \ε\ί\χ\α\τ\ε\,\ \ε\ί\χ\α\ν\)\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Σ\υ\ν\τ\ε\λ\.\ \Μ\έ\λ\λ\.\<\/td\>
\<td\ colspan\=\"6\"\>\θ\α\ \έ\χ\ω\ \(\θ\α\ \έ\χ\ε\ι\ς\,\ \θ\α\ \έ\χ\ε\ι\,\ \θ\α\ \έ\χ\ο\υ\μ\ε\,\ \θ\α\ \έ\χ\ε\τ\ε\,\ \θ\α\ \έ\χ\ο\υ\ν\)\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή\<\/td\>
\<td\ colspan\=\"6\"\>\ν\α\ \έ\χ\ω\ \(\ν\α\ \έ\χ\ε\ι\ς\,\ \ν\α\ \έ\χ\ε\ι\,\ \ν\α\ \έ\χ\ο\υ\μ\ε\,\ \ν\α\ \έ\χ\ε\τ\ε\,\ \ν\α\ \έ\χ\ο\υ\ν\)\ \λ\υ\μ\έ\ν\ο\<\/td\>
\<\/tr\>
\<\/table\>"""

metoxi = """\<td\ rowspan\=\"6\"\ align\=\"center\"\>\<a\ href\=\"\/wiki\/(.*?)\"\ title\=\"(.*?)\"\>(?P<METOXI2>.*?)\<\/a\>
\<\/td\>"""

mono_exakolouthitikoi = """\<tr\>
\<th\>\π\ρ\ό\σ\ω\π\α
\<\/th\>
\<th\>\Ε\ν\ε\σ\τ\ώ\τ\α\ς
\<\/th\>
\<th\>\Π\α\ρ\α\τ\α\τ\ι\κ\ό\ς
\<\/th\>
\<th\>\Ε\ξ\.\ \Μ\έ\λ\λ\.
\<\/th\>
\<th\>\Υ\π\ο\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\>\Π\ρ\ο\σ\τ\α\κ\τ\ι\κ\ή
\<\/th\>
\<th\ align\=\"center\"\>\Μ\ε\τ\ο\χ\ή
\<\/th\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<EX_MEL_A_ENIKO>.*?)
\<\/td\>
\<td\>(?P<YPOT_EX_A_ENIKO>.*?)
\<\/td\>
\<td\>
\<\/td\>
\<td\ rowspan\=\"6\"\ align\=\"center\"\>(?P<METOXI>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_B_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_ENIKO>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \ε\ν\ι\κ\.
\<\/td\>
\<td\>(?P<ENEST_G_ENIKO>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_ENIKO>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\α\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_A_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_A_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\β\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_B_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_B_PL>.*?)
\<\/td\>
\<td\>\θ\α (.*?)
\<\/td\>
\<td\>\ν\α (.*?)
\<\/td\>
\<td\>(?P<PROST_ENEST_B_PL>.*?)
\<\/td\>\<\/tr\>
\<tr\>
\<td\ style\=\"background\:\#c0c0c0\"\>\γ\'\ \π\λ\η\θ\.
\<\/td\>
\<td\>(?P<ENEST_G_PL>.*?)
\<\/td\>
\<td\>(?P<PARATATIKOS_G_PL>.*?)
\<\/td\>
\<td\>\θ\α\ (.*?)
\<\/td\>
\<td\>\ν\α\ (.*?)
\<\/td\>
\<td\>"""

#print(re.sub(r'\\\n','\n',re.escape(t))) # this produces the above
	
def s(s):
	if s == None:
		return ''
	return s

def add_verb(form,greek_pos,lemma,person,number,tense,mood,aspect,verbform,voice):
	all_forms = get_forms(form)
	for i in all_forms:
		#print(i +' '+ lemma + ' ' + str(s(person)) + ' '+s(number)+' '+s(tense)+' '+s(mood)+' '+s(aspect)+' '+s(verbform)+' '+s(voice))
		wword(i,lemma,'VERB',person=person,number=number,tense=tense,mood=mood,aspect=aspect,verbform=verbform,voice=voice,greek_pos=greek_pos)


def parse_verb(html,code,lemma):
	#TODO εντοπισμός {{παθ|}}
	#μετοχές {{μτχππ| και {{μτχπε|
	# TODO μετοχές ούμενος
	v = 'Act'
	res = re.search("\<div class=\"NavHead\" align=\"left\">&#160; &#160; Ενεργητική φωνή</div>",html,re.DOTALL|re.UNICODE)
	if res == None:
		v = 'Pass'
	detected = 0
	for a in re.finditer(energ,html,re.DOTALL|re.UNICODE):
		detected = 1
		if v == 'Pass' and form_exists(a.group('ENEST_A_ENIKO'),'VERB'):#Αν έχουμε βάλει το παθητικό λήμμα
			cur.execute("DELETE FROM words WHERE lemma = \'%s\'"%(esc(a.group('ENEST_A_ENIKO'))))

		if v == 'Pass':
			met = re.search(metoxi,html,re.DOTALL|re.UNICODE)
			if met != None:
				print(' Η μετοχή είναι: ' + met.group('METOXI2'),end='')
				wword(met.group('METOXI2'),lemma,'VERB',greek_pos='METOXI_PP',gender='Masc',ptosi='Nom',number='Sing',aspect='Perf',verbform='Part',voice='Pass')
			else:
				print(' Δεν βρέθηκε μετοχή',end='')
		add_verb(a.group('ENEST_A_ENIKO'),'ENEST_A_ENIKO',lemma,1,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_ENIKO'),'ENEST_B_ENIKO',lemma,2,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_ENIKO'),'ENEST_G_ENIKO',lemma,3,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_A_PL'),'ENEST_A_PL',lemma,1,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_PL'),'ENEST_B_PL',lemma,2,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_PL'),'ENEST_G_PL',lemma,3,'Plur','Pres','Ind','Imp','Fin',v)
		
		add_verb(a.group('AOR_A_ENIKO'),'AOR_A_ENIKO',lemma,1,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_B_ENIKO'),'AOR_B_ENIKO',lemma,2,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_G_ENIKO'),'AOR_G_ENIKO',lemma,3,'Sing','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_A_PL'),'AOR_A_PL',lemma,1,'Plur','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_B_PL'),'AOR_B_PL',lemma,2,'Plur','Past','Ind','Perf','Fin',v)
		add_verb(a.group('AOR_G_PL'),'AOR_G_PL',lemma,3,'Plur','Past','Ind','Perf','Fin',v)

		add_verb(a.group('PARATATIKOS_A_ENIKO'),'PARATATIKOS_A_ENIKO',lemma,1,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_ENIKO'),'PARATATIKOS_B_ENIKO',lemma,2,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_ENIKO'),'PARATATIKOS_G_ENIKO',lemma,3,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_A_PL'),'PARATATIKOS_A_PL',lemma,1,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_PL'),'PARATATIKOS_B_PL',lemma,2,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_PL'),'PARATATIKOS_G_PL',lemma,3,'Plur','Past','Ind','Imp','Fin',v)

		add_verb(a.group('METOXI'),'METOXI_EE' if v == 'Act' else 'METOXI_PE',lemma,None,None,None,None,'Imp','Conv',v)
		add_verb(a.group('AOR_APAREMFATO'),'AOR_APAREMFATO',lemma,None,None,None,None,'Perf','Inf',v)
		
		add_verb(a.group('PROST_ENEST_B_ENIKO'),'PROST_ENEST_B_ENIKO',lemma,2,'Sing',None,'Imp','Ind','Fin',v) # Λογικά Ind 
		add_verb(a.group('PROST_ENEST_B_PL'),'PROST_ENEST_B_PL',lemma,2,'Sing',None,'Imp','Ind','Fin',v)
		
		add_verb(a.group('PROST_AOR_B_ENIKO'),'PROST_AOR_B_ENIKO',lemma,2,'Sing',None,'Imp','Perf','Fin',v)
		add_verb(a.group('PROST_AOR_B_PL'),'PROST_AOR_B_PL',lemma,2,'Sing',None,'Imp','Perf','Fin',v)
		
		#γιατί οριστική για αυτό;??????
		add_verb(a.group('AOR_YPOT_A_ENIKO'),'AOR_YPOT_A_ENIKO',lemma,1,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_B_ENIKO'),'AOR_YPOT_B_ENIKO',lemma,2,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_G_ENIKO'),'AOR_YPOT_G_ENIKO',lemma,3,'Sing',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_A_PL'),'AOR_YPOT_A_PL',lemma,1,'Plur',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_B_PL'),'AOR_YPOT_B_PL',lemma,2,'Plur',None,'Ind','Perf','Fin',v)
		add_verb(a.group('AOR_YPOT_G_PL'),'AOR_YPOT_G_PL',lemma,3,'Plur',None,'Ind','Perf','Fin',v)
		v = 'Pass'
		
	v = 'Act'
	a = re.search(mono_exakolouthitikoi,html,re.DOTALL|re.UNICODE)
	if detected == 0 and a != None:
		add_verb(a.group('ENEST_A_ENIKO'),'ENEST_A_ENIKO',lemma,1,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_ENIKO'),'ENEST_B_ENIKO',lemma,2,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_ENIKO'),'ENEST_G_ENIKO',lemma,3,'Sing','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_A_PL'),'ENEST_A_PL',lemma,1,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_B_PL'),'ENEST_B_PL',lemma,2,'Plur','Pres','Ind','Imp','Fin',v)
		add_verb(a.group('ENEST_G_PL'),'ENEST_G_PL',lemma,3,'Plur','Pres','Ind','Imp','Fin',v)
		
		add_verb(a.group('PARATATIKOS_A_ENIKO'),'PARATATIKOS_A_ENIKO',lemma,1,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_ENIKO'),'PARATATIKOS_B_ENIKO',lemma,2,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_ENIKO'),'PARATATIKOS_G_ENIKO',lemma,3,'Sing','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_A_PL'),'PARATATIKOS_A_PL',lemma,1,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_B_PL'),'PARATATIKOS_B_PL',lemma,2,'Plur','Past','Ind','Imp','Fin',v)
		add_verb(a.group('PARATATIKOS_G_PL'),'PARATATIKOS_G_PL',lemma,3,'Plur','Past','Ind','Imp','Fin',v)
		
		add_verb(a.group('PROST_ENEST_B_ENIKO'),'PROST_ENEST_B_ENIKO',lemma,2,'Sing',None,'Imp','Ind','Fin',v) # Λογικά Ind 
		add_verb(a.group('PROST_ENEST_B_PL'),'PROST_ENEST_B_PL',lemma,2,'Sing',None,'Imp','Ind','Fin',v)
		detected = 1;
		
	#ΤODO VerbForm=Conv για τις μετοχές οντας, VerbForm=Inf για τα απαρρέμφατα,VerbForm=Part με Voice=Pass για τις μετομές που προκείπτουν από ρήμα
	#για τις άλλες μετοχές ADJ,VerbForm=Fin για τα άλλα
	
	if detected == 0:
		wword(lemma,lemma,'VERB',tags="Incomplete")

import logging
import re

import requests
import six
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from immeuble.models import AutoName

LIST_AUTONAME = ('Abélia',
                 'Abricotier',
                 'Absinthe',
                 'Abutilon',
                 'Abutilondu Brésil',
                 'Acacia',
                 'Acalypha',
                 'Acanthe',
                 'Âche oufaux-cresson',
                 'Achillée',
                 'Aconit',
                 'Acorus',
                 'Adenostyle',
                 'Adonis annua',
                 'Aechmea',
                 'Aeonium',
                 'Aeschy-nanthus',
                 'Agapanthe',
                 'Agastache',
                 'Agave',
                 'Agerate',
                 'Aigremoine',
                 'Ail',
                 'Ailornemental',
                 'Airellerouge',
                 'Ajonc',
                 'Akebia',
                 'Alchemille',
                 'Alfa',
                 'Allamandacathartica',
                 'Alocasia',
                 'Aloe vera',
                 'Alstroemeria',
                 'Alternan-thera',
                 'Alyssum',
                 'Amandier',
                 'Amarante',
                 'Amaryllis',
                 'Amélanchier du Canada',
                 'Ammi',
                 'Amorpho-phallus',
                 'Amourette',
                 'Ananas',
                 'Ancolie',
                 'Anémone de Caen',
                 'Anemone de Haller',
                 'Anémone du Japon',
                 'Anémone Sylvie',
                 'Aneth',
                 'Angélique',
                 'Anigozanthos',
                 'Anisodontea',
                 'Anthemis',
                 'Anthurium',
                 'Apios',
                 'Aponogeton distachyos',
                 'Aptenia',
                 'Arabette',
                 'Aralia',
                 'Araucaria',
                 'Arbousier',
                 'Arbre àpapillons',

                 'Arbre àperruques',
                 'Arbre aux anemones',
                 'Arbre aux faisans',
                 'Arbre aux gentianes',
                 'Arbre de judée',
                 'Arbre du voyageur',
                 'Arbrea suif',

                 'Arbre bouteille',
                 'Arbre caramel',
                 'Arbrede soie',
                 'Ardisia crenata',
                 'Arganier',
                 'Argousier',
                 'Aristoloche',
                 'Armeria',
                 'Arnica',
                 'Aronia',

                 'Arroche',
                 'Artichaut',
                 'Arum des fleuristes',
                 'Arum puant',
                 'Asclépiade',
                 'Asparagus',
                 'Asperge',
                 'Asphodeline',
                 'Aster',
                 'Astilbe',
                 'Astrance',
                 'Aubépine',
                 'Aubergine',
                 'Aubriete',
                 'Aucuba',
                 'Aulne',
                 'Avocatier',
                 'Azalee',
                 'Azara',
                 'Bacopa',
                 'Baguenaudier',
                 'Balisier',
                 'Ballote',
                 'Balsamine',
                 'Bambou de la chance',
                 'Bambou',
                 'Bananier musa velutina',
                 'Bananier fruitier',
                 'Bananier musa basjoo',
                 'Bananier nain chinois',
                 'Bananiers ikkimensis',
                 'Banksia',
                 'Bardane',
                 'Basilic',
                 'Baumede Galaad',
                 'Beaucarnea',
                 'Bégoniagrandis',
                 'Bégoniahorticole',
                 'Belladone',
                 'Bellede jour',
                 'Bellede nuit',
                 'Benoite',
                 'Berberis',
                 'Berce',
                 'Bergenia',
                 'Bermudienne',
                 'Beschor-neria',
                 'Bétoine ouépiaire',
                 'Bette',
                 'Betterave',
                 'Bidens',
                 'Bignone',
                 'Bijouxd\'Ophar',
                 'Blétilla',
                 'Bleuet',
                 'Bougainvillier',
                 'Bouillonblanc',
                 'Bouleau',
                 'Bourrache',
                 'Bourreaudes arbres',
                 'Boutond\'or',
                 'Bromeliacées',
                 'Brugmansia',
                 'Brunfelsia',
                 'Bruyère',
                 'Bryone',
                 'Bugle',
                 'Buglosse',
                 'Buis',
                 'Buplèvre',
                 'Cacaoyer',
                 'Cactus',
                 'Caesalpina',
                 'Cafeier',
                 'Caille-lait',
                 'Calamondin',
                 'Calathea',
                 'Calcéolaire',
                 'Calebasse',
                 'Calliandra',
                 'Callicarpa',
                 'Callistemon',
                 'Callunavulgaris',
                 'Calthapalustris',
                 'Camassia',
                 'Camélia',
                 'Camomille',
                 'Campanule',
                 'Campélia',
                 'Canna',
                 'Canne deProvence',
                 'Caoutchouc',
                 'Capsicum',
                 'Capucine',
                 'Capucinetubéreuse',
                 'Cardamine',
                 'Cardère',
                 'Carexflagellifera',
                 'Carotte',
                 'Carthame',
                 'Caryopteris',
                 'Cassia',
                 'Cassissier',
                 'Catalpa',
                 'Ceanothe',
                 'Cèdrede l\'Atlas',
                 'Cèdredu Liban',
                 'Céleri rave',
                 'Celosie',
                 'Ceratostigma',
                 'Cerfeuil',
                 'Cerfeuiléternel',
                 'Cerisierà fleurs',
                 'Cerisiercerise',
                 'Ceropegia',
                 'Cestrum',
                 'Chamae-cyparis',
                 'Chanvre',
                 'Chapeaumexicain',
                 'Chardon',
                 'Charme',
                 'Châtaignier châtaigne',
                 'Châtaignierd\'Australie',
                 'Chayote',
                 'Chelidoine',
                 'Chêne rouged\'Amérique',
                 'Chêne pédonculé',
                 'Cheneblanc',
                 'Cheneliege',
                 'Chênepalustre',
                 'Chenevert',
                 'Chevrefeuille',
                 'Chicoree',
                 'Chimonanthuspraecox',
                 'Chlorophytum',
                 'Chorisia',
                 'Choux',
                 'Chouxd\'ornement',
                 'Chouxmaritimes',
                 'Chrysanthème',
                 'Chrysanthème à carène',
                 'Ciboulette',
                 'Cimicifuga',
                 'Cinéraire des fleuristes',
                 'Cinéraire maritime',
                 'Ciste',
                 'Citronvert',
                 'Citronnelle',
                 'Citronnier',
                 'Citronniercaviar',
                 'Citrouille',
                 'Clématite',
                 'Clématite armandii',
                 'Clémentinier',
                 'Cléome',
                 'Clérodendron de Thomson',
                 'Clerodendronbungei',
                 'Clérodendrontrichotomum',
                 'Clivia',
                 'Cobée',
                 'Coca',
                 'Cochliostema',
                 'Coeur de marie',
                 'Cognassier',
                 'Cognassier du Japon',
                 'Cola',
                 'Colchique',
                 'Coléus',
                 'Colletiaparadoxa',
                 'Colocasia',
                 'Columnea',
                 'Colza',
                 'Combava',
                 'Comméline commune',
                 'Concombre',
                 'Concombredes ânes',
                 'Consoude',
                 'Convolvulus',
                 'Coprosma',
                 'Coquelicot',
                 'Coquelourde',
                 'Corbeilled\'argent',
                 'Corbeilled\'or',
                 'Cordylineaustralis',
                 'Cordylineindivisa',
                 'Cordylineterminalis',
                 'Coreopsis',
                 'Coriandre',
                 'Cornouiller',
                 'Cornouiller du Japon',
                 'Cornouillerd\'Amérique',
                 'Coronille',
                 'Corynephorus',
                 'Cosmos',
                 'Cosmoschocolat',
                 'Cotoneaster',
                 'Cotyledon',
                 'Coucou',
                 'Courgette',
                 'Coussin de belle-mère',
                 'Crassule',
                 'Cressonde fontaine',
                 'Cressonde terre',
                 'Crinumpowellii',
                 'Crocosmia',
                 'Crocus',
                 'Croix deMalte',
                 'Croton',
                 'Cryptanthus',
                 'Cryptomeriajaponica',
                 'Cténanthe',
                 'Cuphéa',
                 'Cupidone',
                 'Curcuma',
                 'Cyca',
                 'Cyclamen',
                 'Cyclanthère',
                 'Cymbalaire',
                 'Cyprèschauve',
                 'Cyprèsde Leyland',
                 'Cytise',
                 'Dahlia',
                 'Daphnée',
                 'Daphneemezereum',
                 'Dasylirion',
                 'Datura',
                 'Daturastramoine',
                 'Delairea ouseneçon',
                 'Delphinium',
                 'Dentelaire',
                 'Deutzia',
                 'Diascia',
                 'Dieffenbachia',
                 'Digitale',
                 'Dionée',
                 'Dipladenia',
                 'Dizygotheca',
                 'Doronique',
                 'Dracaena',
                 'Dragonnier',
                 'Drosera',
                 'Eccrémocarpe',
                 'Échalote',
                 'Echeveria',
                 'Edelweiss',
                 'Edgeworthiachrysantha',
                 'Eleagnus',
                 'Élymedes sables',
                 'Endive',
                 'Épicéaglauca',
                 'Épilobe',
                 'Épimède',
                 'Épinard',
                 'Épinardgrimpant',
                 'Épine du Christ',
                 'Episcia',
                 'Érableà sucre',
                 'Érabledu Japon',
                 'Eremurus',
                 'Érigeron',
                 'Erythrina',
                 'Escallonia',
                 'Estragon',
                 'Eucalyptus',
                 'Eucomis oufleur ananas',
                 'Euonymusou fusain',
                 'Eupatoire',
                 'Euphorbe',
                 'Euphorbearborescente',
                 'Exochorda',
                 'Faux nénuphar',
                 'Faux-poivrier',
                 'poivre rose',
                 'Fenouil',
                 'Fenouilmarin',
                 'Férulefétide',
                 'Fetuque',
                 'Fèves',
                 'Fevier',
                 'Ficoide',
                 'Ficus',
                 'Ficusginseng',
                 'Figuierbarbarie',
                 'Figuierfigue',
                 'Fittonia',
                 'Flamboyant',
                 'Fléoledes prés',
                 'Fleuréventail',
                 'Fockéa',
                 'Forsythia',
                 'Fougèreappartement',
                 'Fougerearborescente',
                 'Fougèrecapillaire',
                 'Fougerecorne-de-cerf',
                 'Fougèredryopteris',
                 'Fraisierdes-Indes',
                 'Fraisierfraise',
                 'Framboisier',
                 'Frangipanier',
                 'Freesia',
                 'Frémonto-dendron',
                 'Frêne',
                 'Fritillairede Perse',
                 'Fritillaireimperialis',
                 'Fritillairepintade',
                 'Fuchsia',
                 'Fuchsiadu cap',
                 'Fusaineurope',
                 'Gaillarde',
                 'Garance',
                 'Gardenia',
                 'Garrya',
                 'Gaultherie',
                 'Gaura',
                 'Gazania',
                 'Genet',
                 'Genetrampant',
                 'Genevrier',
                 'Gentiane',
                 'Géraniumpelargonium',
                 'Geraniumvivace',
                 'Gerbera',
                 'Germandree',
                 'Gillenia',
                 'Ginkgobiloba',
                 'Giroflee',
                 'Glaieul',
                 'Gloiredes neiges',
                 'Gloriosa',
                 'Glycine',
                 'Godetiaou clarkia',
                 'Goji',
                 'Gomphocarpus',
                 'Gomphrena',
                 'Goyavier',
                 'Graptopetalum',
                 'Grassette',
                 'Gratiole',
                 'Grenadier',
                 'Grevillea',
                 'Griffesde sorcière',
                 'Griselinia',
                 'Groseillerà fleurs',

                 'Groseillier',
                 'Gui',
                 'Guimauve',
                 'Gunnera',
                 'Haemanthus',
                 'Hakéa',
                 'Hamamélis',
                 'Haricot rouged\'espagne',
                 'Haworthia',
                 'Hechtia',
                 'Hedychium',
                 'Helenium',
                 'Heliamphora',
                 'Heliantheme',
                 'Héliotrope',
                 'Hélixine',
                 'Helléborine',
                 'Hemerocalle',
                 'Herbe aux chats',
                 'Herbe de la pampa',
                 'Herbeaux perruches',
                 'Herbedu Japon',
                 'Hêtrepourpre',
                 'Heuchera',
                 'Hibiscus desjardins',
                 'Hibiscus ourose de chine',
                 'Hibiscuscoccineus',
                 'Hibiscusmoscheutos',
                 'Hibiscustrionum',
                 'Hippuris oupesse d\'eau',
                 'Homalomena',
                 'Hortensia',
                 'Hortensiagrimpant',
                 'Hosta',
                 'Houblon',
                 'Houttuynia',
                 'Houx',
                 'Hoya',
                 'Hydrangea',
                 'Hypericum',
                 'Hysope',
                 'Iberis',
                 'If',
                 'Immortelleà bractées',
                 'Impatience',
                 'Imperatacylindrica',
                 'Indigofera',
                 'Inule',
                 'Ipheion',
                 'Iresine',
                 'Iris aquatique',
                 'Iris de Hollande',
                 'Iris des jardin',
                 'Isotoma',
                 'Jacinthe',
                 'Jacinthe d\'eau',
                 'Jacobinia',
                 'Jasmin d\'hiver',
                 'Jasminofficinal',
                 'Jonc fleuriou butome',
                 'Jonc',
                 'Jonquilles',
                 'Joubarbe',
                 'Jujubier',
                 'Juliennedes Dames',
                 'Juniperus',
                 'Jussie',
                 'Kaki: fruit duplaqueminier',
                 'Kalanchoe',
                 'Kalmia',
                 'Kerria',
                 'Kiwi ouactinidia',
                 'Knautia',
                 'Kniphofia',
                 'Kochia',
                 'Koeleria',
                 'Kolkwitzia',
                 'Kumquat',
                 'Laitue',
                 'Lamier',
                 'Lantana',
                 'Larme de job',
                 'Lathréeclandestine',
                 'Laurier duPortugal',
                 'Laurier rose',
                 'Laurier sauce',
                 'Laurier tin',
                 'Laurier d\'Alexandrie',
                 'Laurierdes bois',
                 'Laurierpalme',
                 'Lavande',
                 'Lavatère',
                 'Lentille d\'eau',
                 'Léonotis',
                 'Léptospermum',
                 'Leucothoe',
                 'Lewisia',
                 'Liatris',
                 'Lierre',
                 'Lierreterrestre',
                 'Ligularia',
                 'Lilas',
                 'Lilasdes Indes',
                 'Limonium oustatice',
                 'Lin',
                 'Liquidambar',
                 'Liriope',
                 'Lis descrapauds',
                 'Lis',
                 'Liseron',
                 'Litchi',
                 'Lithodoradiffusa',
                 'Livèche',
                 'Loasa',
                 'Lobélia',
                 'Loniceragracilipes',
                 'Loniceranitida',
                 'Loropetalum',
                 'Lotier',
                 'Lotus',
                 'Lupin',
                 'Luzerne',
                 'Lysichiton',
                 'Lysimachianummularia',
                 'Mâche',
                 'Macrozamia',
                 'Magnoliagrandiflora',
                 'Magnoliasoulangiana',
                 'Mahoberberis',
                 'Mahonia',
                 'Mainde Bouddha',
                 'Maïs',
                 'Malvaviscus',
                 'Mandragore',
                 'Maranta',
                 'Margousierou mélia',
                 'Marguerite',
                 'Margueritedu Cap',
                 'Marjolaineou origan',
                 'Marronnier d\'Inde',
                 'Massette',
                 'Mauve',
                 'Medinilla',
                 'Melaleuca',
                 'Mélampodium',
                 'Mélèze',
                 'Mélianthus',
                 'Mélisse',
                 'Melon',
                 'Menthe',
                 'Mentheaustralienne',
                 'Merisier',
                 'Micocoulier',
                 'Millepertuis',
                 'Millet',
                 'Mimosa',
                 'Miscanthussinensis',
                 'Misère',
                 'Molène',
                 'Monarde',
                 'Monnaie du pape',
                 'Morelle de Balbis',
                 'Morelle',
                 'Moutardenoire',
                 'Muehlen-beckia',
                 'Muflier (gueulede loup)', 'Muguet',
                 'Mûrier',
                 'Mûrierde Chine',
                 'Muscari',
                 'Myosotis',
                 'Myrte',
                 'Myrtille',
                 'Nandina',
                 'Nashi',
                 'Navet',
                 'Néflier',
                 'Néflierdu Japon',
                 'Neillia',
                 'Némésia',
                 'Nénuphar',
                 'Nepenthes',
                 'Nertera',
                 'Nicandra',
                 'Nielle des blés',
                 'Nigellede Damas',
                 'Niveoleprintanière',
                 'Noisetier',
                 'Nombrilde venus',
                 'Noyer',
                 'Noyer d\'Amérique',
                 'Oeillet-couche',
                 'Oeillet d\'inde',
                 'Oeilletde poète',
                 'Oenothere',
                 'Oignon',
                 'Oignongrimpant',
                 'Oiseaude paradis',
                 'Oléaria',
                 'Olivier',
                 'Olivierde bohème',
                 'Omphalodes',
                 'Onagre',
                 'Ophiopogon',
                 'Oranger',
                 'Orangerdu mexique',
                 'Orchidée',
                 'Orchis',
                 'Oreille d\'ours',
                 'Oreillede souris',
                 'Orgemaritime',
                 'Orme blanc',
                 'Ornithogale',
                 'Ornithogaledubium',
                 'Orpin ousedums',
                 'Ortie',
                 'Oseille',
                 'Osier',
                 'Osmanthus',
                 'Osmarea',
                 'Osmonde',
                 'Osteospermum',
                 'Ostrya',
                 'Othonna',
                 'Oxalis',
                 'Pachira',
                 'Pachysandra',
                 'Pachystachys',
                 'Palmier bleudu Mexique',
                 'Palmier dattier',
                 'Palmier de Bismarck',
                 'Palmier deCalifornie',
                 'Palmier deMadagascar',
                 'Palmier nain',
                 'Palmier:le cocotier',
                 'Palmier du Brésil',
                 'Palmierareca',
                 'Palmierargentin',
                 'Palmierbambou',
                 'Palmierchamaedorea',
                 'Palmierde Chine',
                 'Palmierdes canaries',
                 'Palmierdu Chili',
                 'Palmierhawaïen',
                 'Palmierle kentia',
                 'Palmierlicuala',
                 'Palmierlivistona',
                 'Palmierphoenix',
                 'Palmiertrithrinax',
                 'Panais',
                 'Pandanus',
                 'Pandoréa',
                 'Papaye',
                 'Papyrus',
                 'Paquerette',
                 'Parrotia',
                 'Parrotiopsis',
                 'Passiflore',
                 'Patate douce',
                 'Paulownia',
                 'Pavot bleu',
                 'Pavot cornu',
                 'Pavot en arbre',
                 'Pavot jaune',
                 'Pavot',
                 'Pavot de californie',
                 'Pavot d\'Islande',
                 'Pêcher',
                 'Pensée',
                 'Penstemon',
                 'Pentas',
                 'Peperomia',
                 'Perce-neige',
                 'Pernettya',
                 'Perovskia',
                 'Persicaria',
                 'Persil',
                 'Pervenche deMadagascar',
                 'Pervenche',
                 'Pétasite',
                 'Petits-pois',
                 'Petunia',
                 'Peuplier',
                 'Phillyreaangustifolia',
                 'Philodendron',
                 'Phlox',
                 'Phormium',
                 'Photinia',
                 'Physalis',
                 'Physocarpe',
                 'Phytolaccadioica',
                 'Pieris',
                 'Pigamon',
                 'Piléa',
                 'Piment',
                 'Pimprenelle',
                 'Pin de norfolk',
                 'Pin noir',
                 'Pin parasol',
                 'Pinsylvestre',
                 'Pisonia',
                 'Pissenlit',
                 'Pistia',
                 'Pittosporum',
                 'Pivoine',
                 'Plantain',
                 'Plantain d\'eau',
                 'Plante à curry',
                 'Plantepapillon',
                 'Platane',
                 'Platycodon',
                 'Plectranthus',
                 'Poinsettia ou étoile de Noël',
                 'Poireau',
                 'Poirier',
                 'Poisde senteur',
                 'Poivron',
                 'Polemonium',
                 'Polygala',
                 'Polygonum',
                 'Pomelo',
                 'Pommede terre',
                 'Pommier',
                 'Pommieramour',
                 'Pommier d\'ornement',
                 'Poncirus',
                 'Pontederia',
                 'Potentille',
                 'Potentillepalustre',
                 'Pourpier',
                 'Prêle',
                 'Primevère',
                 'Primevèreauricule',
                 'Primevèredu Japon',
                 'Protéa',
                 'Prunellier',
                 'Prunier',
                 'Prunussubhirtella',
                 'Prunustomentosa',
                 'Pulmonaire',
                 'Pyracantha',
                 'Pyrostegia',
                 'Queue delièvre',
                 'Queue derat',
                 'Radis',
                 'Raifort',
                 'Raiponce',
                 'Raisind\'Amérique',
                 'Ramondie',
                 'Réglisse',
                 'Reine-marguerite',
                 'Reinedes prés',
                 'Renoncule',
                 'Renouéedu Japon',
                 'Rhipsalis',
                 'Rhododendron',
                 'Rhoeo',
                 'Rhubarbe',
                 'Ricin',
                 'Robinier',
                 'Rodgersia',
                 'Rohdea',
                 'Romarin',
                 'Ronce',
                 'Ronceet mûres',
                 'Rose de Noël',
                 'Rosedu désert',
                 'Rosemalaisie',
                 'Rose porcelaine',
                 'Rosetrémière',
                 'Roseaupanaché',
                 'Rosier',
                 'Rotheca',
                 'Rubande bergère',
                 'Rubanier',
                 'Rudbeckia',
                 'Rue fétide',
                 'Ruellia',
                 'Rumex',
                 'Ruscus',
                 'Sainfoin',
                 'Saintpaulia',
                 'Salicaire',
                 'Salicorne',
                 'Salpiglossis',
                 'Salsepareille',
                 'Salsifis',
                 'Salvinia',
                 'Sanseveria',
                 'Santoline',
                 'Sanvitalia',
                 'Sapin',
                 'Saponaire',
                 'Sarracenia',
                 'Sarrazin',
                 'Sarriette',
                 'Sauge',
                 'Sauge argentée',
                 'Sauge jerusalem',
                 'Sauge officinale',
                 'Saule-crevette',
                 'Saule',
                 'Savonnier',
                 'Saxifrage',
                 'Scabieuse',
                 'Sceau de salomon',
                 'Schefflera',
                 'Schizostylis',
                 'Scindapsusou pothos',
                 'Scleranthus',
                 'Sedum',
                 'Sedumpalmeri',
                 'Seneciorowleyanus',
                 'Séquoia',
                 'Seringat',
                 'Shiso',
                 'Silène',
                 'Skimmiajaponica',
                 'Smilacinaracemosa',
                 'Solanumjasminoïdes',
                 'Solanumquitoense',
                 'Solidago ouverge d\'or',
                 'Sophora',
                 'Sophora microphylla',
                 'Sorbierdes oiseaux',
                 'Sorgho',
                 'Souci',
                 'Sparaxis',
                 'Spathiphyllum',
                 'Spiree',
                 'Stapélia',
                 'Staphylea colchica',
                 'Stellaire',
                 'Stephanotis',
                 'Stevia',
                 'Streptocarpus',
                 'Sureau',
                 'Suzanneaux yeux noirs',
                 'Symphorine',
                 'Syngonium',
                 'Tabac',
                 'Tamaris',
                 'Tanaisie',
                 'Telopea',
                 'Tetrapanax',
                 'Thalia',
                 'Théier',
                 'Thunber giagrandiflora',
                 'Thuya',
                 'Thym',
                 'Tiarella',
                 'Tibouchina',
                 'Tillandsia',
                 'Tilleul',
                 'Tithonia',
                 'Tolmiede menzies',
                 'Tomate',
                 'Topinambour',
                 'Tournesol',
                 'Tradescantia',
                 'Trèfle',
                 'Trèfle d\'eau',
                 'Troène',
                 'Trolle',
                 'Tulbaghia',
                 'Tulipes',
                 'Tulipierde Virginie',
                 'Uniola',
                 'Valeriane',
                 'Vancouveria',
                 'Vanille',
                 'Veronique',
                 'Véronique',
                 'Verveine de buenos aires',
                 'Verveine',
                 'Vigne',
                 'Vigne d\'appartement',
                 'Vignevierge',
                 'Vinaigrierou sumac',
                 'Violette',
                 'Viorne',
                 'Viperine',
                 'Vitex',
                 'Volubilis',
                 'Wattakaka',
                 'Weigelia',
                 'Westringia',
                 'Xanthosoma',
                 'Yucca',
                 'Zamioculcas',
                 'Zantedeschia',
                 'Zanthoxylum',
                 'Zelkova',
                 'Zenobia',
                 'Zinnia',
                 'Zygocactus')

logger = logging.getLogger(__name__)


def create_autoname():
    """
    Insert each object in type_dependance list in according table if not exist
    :return: num_updated: int, num_created: int
    :raise ValidationError:
    """
    num_created = 0
    for auto in LIST_AUTONAME:
        nb = AutoName.objects.filter(libelle=auto).count()
        if nb > 0:
            continue

        try:
            AutoName.objects.create(libelle=auto)
            num_created = num_created + 1
        except ValidationError as e:
            logger.debug(f"error while creating dependecy: {e}")

    return num_created

class Command(BaseCommand):
    help = "Générer des valeurs qui serviront à autonommer les immeubles"

    def handle(self, *args, **options):
        num_created = create_autoname()
        self.stdout.write(
            "Autoname creer avec succès.  "
            "%s autoname were updated, %s autoname were created." % (0, num_created))

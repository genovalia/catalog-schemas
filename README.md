# Schéma de catalogue et de jeux de données pour Genovalia

Ce document utilise le format `yaml` pour représenter des structures afin de faciliter la lecture et permettre l'ingestion par une machine ultérieurement.

## Liens important
- [Sépcification DCAT 2.0](https://www.w3.org/TR/vocab-dcat-2/)
- [json+ld](https://www.w3.org/TR/json-ld/)

## Namespaces
- dcat: http://www.w3.org/ns/dcat#
- dcterms: http://purl.org/dc/terms/
- foaf: http://xmlns.com/foaf/0.1/
- xsd: http://www.w3.org/2001/XMLSchema#
- prov: https://www.w3.org/ns/prov#

## Tour d'horizon de DCAT
DCAT est un vocabulaire RDF pour décrire des catalogues de données. Il est utilisé pour représenter des catalogues de jeux de données, des jeux de données eux-mêmes, ainsi que les distributions de ces jeux de données.

On y retrouve donc dans le vocabulaire des éléments comme `dcat:Catalog` et `dcat:Dataset`. Ces éléments contiennent des propriétés, comme `title`, `publisher` et `theme`. Ces propriétés sont décrites par des vocabulaires; la propriété `title` est décrite par le terme de vocabulaire `dcterms:title`, afin qu'une machine comprenne que cette propriété est un titre. Finalement, chaque propriété a une valeur, qui est représentée par un littéral ou une ressource, généralement reliée à un vocabulaire ou une ontologie.

## Éléments
### Catalogue
Un catalogue est un ensemble de jeux de données. Il est décrit par l'élément `dcat:Catalog`. Un catalogue peut contenir plusieurs jeux de données, chacun étant décrit par l'élément `dcat:Dataset`.

Un Catalogue est en fait un jeu de données de jeu de données (hérite de `dcat:Dataset`, qui hérite de `dcat:Resource`). On y retrouve donc des propriétés qui se répéteront dans les jeux de données, comme `dcterms:title`, `dcterms:description`, `dcterms:publisher`, etc.

## Propriétés

Certaines propriétés sont ommises. La liste suivante représente les propriétés que nous avons jugées pertinentes pour le schéma de Genovalia. Elles sont décrites par des vocabulaires, et sont donc représentées par des URI.

### Ressource
```yaml
dcat:Resource:
    access_rights:
        property: http://purl.org/dc/terms/accessRights
        range: http://purl.org/dc/terms/RightsStatement
        definition: Information about who can access the resource or an indication of its security status.
        note: Pourrait être utilisé pour définir si le jeu de données est public ou si on doit demander l'accès.
    conforms_to:
        property: http://purl.org/dc/terms/conformsTo
        range: http://www.w3.org/2002/07/owl#Thing
        definition: An established standard to which the described resource conforms.
        note: Pourrait être utilisé pour pointer vers un schéma de variables OCA/Semantic Engine.
    contact_point:
        property: https://www.w3.org/ns/dcat#contactPoint
        range: https://www.w3.org/TR/vcard-rdf/#Kind
        definition: Relevant contact information for the cataloged resource.
        note: Dans notre cas, représente l'entité Genovalia dans la majorité des cas
    creator:
        property: http://purl.org/dc/terms/creator
        range: http://xmlns.com/foaf/0.1/Agent
        definition: The entity responsible for producing the resource.
        note: Représente le créateur du jeu de données, généralement les clients de Genovalia
    description:
        property: http://purl.org/dc/terms/description
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: A free-text account of the item.
    title:
        property: http://purl.org/dc/terms/title
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: A name given to the item.
    release_date:
        property: http://purl.org/dc/terms/issued
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: Date of formal issuance (e.g., publication) of the item.
    update_date:
        property: http://purl.org/dc/terms/modified
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: Most recent date on which the item was changed, updated or modified.
    language:
        property: http://purl.org/dc/terms/language
        range: http://purl.org/dc/terms/LinguisticSystem
        definition: A language of the item. This refers to the natural language used for textual metadata (i.e. titles, descriptions, etc) of a cataloged resource (i.e. dataset or service) or the textual values of a dataset distribution
        note: La bibliothèque recommande de prioriser la langue d'origine du jeu de données plutôt que de systématiquement traduire les métadonnées en d'autres langues. À noter qu'il faudra considérer d'autres champs comme les mots clés et le thème pour la recherche dans d'autres langues.
    publisher:
        property: http://purl.org/dc/terms/publisher
        range: http://xmlns.com/foaf/0.1/Agent
        definition: The entity responsible for making the item available.
        note: Dans notre cas, représente l'entité Genovalia dans la majorité des cas. Contrairement à contact_point, qui représente une façon de communiquer, on parle ici d'une représentation de Genovalia comme entité. Peut-être qu'on pourrait stocker cette information dans un URI, comme genovalia.ulaval.ca/about
    identifier:
        property: http://purl.org/dc/terms/identifier
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: A unique identifier of the item.
        note: Représente, dans la majorité de nos cas, le DOI. N'est pas obligé d'être un URI. En fait, comme le jeu de données est représenté par un "id", qui est un DOI, l'identifiant peut être le DOI en format non-URI.
    theme:
        property: https://www.w3.org/ns/dcat#theme
        range: https://www.w3.org/2004/02/skos/core#Concept
        definition: A main category of the resource. A resource can have multiple themes.
        note: Représente le thème du jeu de données, qui est un concept SKOS. On pourrait utiliser les vocabulaires de la bibliothèque pour représenter les thèmes, on trouver un ou des thèmes spécifiques dans des ontologies. Voir https://www.w3.org/2004/02/skos/core#ConceptScheme.
    type:
        property: http://purl.org/dc/terms/type
        range: https://www.w3.org/2000/01/rdf-schema#Class
        definition: The nature or genre of the resource.
        note: Il est recommandé d'utiliser une des valeurs de https://schema.datacite.org/meta/kernel-4.1/include/datacite-resourceType-v4.1.xsd, comme Dataset, Model, Service, Software, etc.
    keyword:
        property: https://www.w3.org/ns/dcat#keyword
        range: https://www.w3.org/2000/01/rdf-schema#Literal
        definition: A keyword or tag describing the resource.
        note: Des mots-clés. Il peut y en avoir plusieurs.
    landing_page:
        property: https://www.w3.org/ns/dcat#landingPage
        range: http://xmlns.com/foaf/0.1/Document
        definition: A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.
    license:
        property: http://purl.org/dc/terms/license
        range: http://purl.org/dc/terms/LicenseDocument
        definition: A legal document under which the resource is made available.
        note: La bibliothèque recommande d'utiliser des licenses existantes. Voir https://creativecommons.org/share-your-work/cclicenses/
    qualified_attribution:
        property: https://www.w3.org/TR/prov-o/#qualifiedAttribution
        range: https://www.w3.org/TR/prov-o/#Attribution
        definition: Link to an Agent having some form of responsibility for the resource
        note: Voir la section Réflexion sur les relations plus bas. Pourrait remplacer creator.
    qalified_relation:
        property: https://www.w3.org/ns/dcat#qualifiedRelation
        range: https://www.w3.org/TR/vocab-dcat-2/#Class:Relationship
        definition: Link to a description of a relationship with another resource
        note: Voir la section Réflexion sur les relations plus bas.
```

### Jeu de données

Le jeu de données hérite des propriétés d'une ressource décrite dans la section précédente. Les champs propres aux jeux de données portent sur la résolution temporelle et spatiale, et sont peut-être moins pertinent pour Genovalia. Ces propriétés sont ommises pour le moment, mais pourraient être ajoutées si nécessaire.

```yaml
dcat:Dataset:
    dataset_distribution:
        property: https://www.w3.org/ns/dcat#distribution
        range: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset
        definition: An available distribution of the dataset.
        note: N'est peut-être pas pertinent
```

### Catalogue

Le catalogue hérite des propriétés d'un jeu de données, et ajoute des propriétés propres aux catalogues.

```yaml
dcat:Catalog:
    homepage:
        property: http://xmlns.com/foaf/0.1/homepage
        range: http://xmlns.com/foaf/0.1/Document
        definition: A homepage of the catalog (a public Web document usually available in HTML).
        note: Techniquement, https://genovalia.ulaval.ca/catalog. Mais ressemble beaucoup à landing_page.
    themes:
        property: https://www.w3.org/ns/dcat#themeTaxonomy
        range: https://www.w3.org/2000/01/rdf-schema#Resource
        definition:  knowledge organization system (KOS) used to classify catalog's datasets and services. It is recommended that the taxonomy is organized in a skos:ConceptScheme, skos:Collection, owl:Ontology or similar, which allows each member to be denoted by an IRI and published as Linked Data.
        note: très similaire à `theme` dans `dcat:Resource`, mais représente un ensemble de thèmes, et non pas un thème spécifique. Représente les thèmes du catalogue, qui sont des concepts SKOS.
    dataset:
        property: https://www.w3.org/ns/dcat#dataset
        range: https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset
        definition: A collection of data that is listed in the catalog.
        note: Tous les jeux de données du catalogue.
```

## Représentation visuelle

### Liste de jeux de données

Sur Borealis, en consultant le catalogue, on peut voir que la liste de jeux de données contient les éléments suivant:
- Titre du jeu de données (title)
- Date de publication (issued)
- un nom (creator) et une source (surement publisher; un des exemples est `Dataverse`)
- un bloc de sitation (peut-être pas nécessaire dans notre cas)
- la description (description)
- un icone représentant le type de jeu de données (type) ou une image

Sur FRDR, la liste de jeux de données semble plus simplifiée:
- Titre du jeu de données (title)
- catégorie? (un exemple est `General / Général`)
- Noms des auteurs (creator)
- Date de publication (issued)

### Page de jeu de données

Sur Borealis, en consultant un jeu de données, on peut voir que la page contient les éléments suivant:
- Titre du jeu de données (title)
- Bloc de citation (peut-être pas nécessaire dans notre cas)
- Description (description)
- Sujet (theme)
- Mots-clés (keyword)
- Publications relatées (related_to, pas mentionné plus haut pour l'instant)
- Licence (license)

On a ensuite une liste d'onglets:
- Les fichiers du jeu de données
- Un onglet de métadonnées
- Un onglet "Terms" qui semble référer à access_rights et license
- Un onglet "Versions" qui liste les versions (un sujet à s'attarder)

L'onglet métadonnées contient les éléments suivants:
- DOI (identifier)
- Date de publication (issued)
- Titre (title)
- Auteurs (creator)
- Point de contact (contact_point)
- Description (description)
- Sujet (theme)
- Mots-clés (keyword)
- Dépositeur
- Date de dépot

Sur FRDR, la page de jeu de données contient les éléments suivants:
- Titre du jeu de données (title)
- Description (description)
- Auteurs (creator)
- Mots-clés (keyword)
- Champ de recherche (themes)
- Date de publication (issued)
- "publisher" (publisher)
- "funder"
- URI (id, identifier)
- liste des fichiers
- Licence (license)
- Bloc de citation

### Design du catalogue de Genovalia

Nous devons déterminer les champs nécessaires que nous comptons afficher sur notre catalogue. En créant notre propre catalogue, nous avons la possibilité de l'adapter à nos besoins et d'éviter les répétitions qui sont nécessaires dans des catalogues plus génériques.

#### Liste de jeux de données

Il va de soit que le titre et la description sont nécessaires. La possibilité d'afficher des mots-clés serait pertinente. Bien que DCAT n'ait pas de concept de métadonnées de mots-clés, il nous serait possible d'assigner des valeurs particulières à des mots-clés spécifiques. Un exemple serait les mots-clés reliés à l'espèce; bien qu'on ne puisse pas représenter l'espèce comme un mot-clé "à part" dans DCAT, nous pourrions lui donner une valeur supplémentaire dans notre système afin qu'il soit affiché dans le catalogue et mis en évidence.

La liste devrait être la plus épurée possible, car elle agit aussi comme résultat de recherche et de filtrage (par mot-clé, thématique, etc.). Les visiteurs doivent être encouragés à cliquer sur un jeu de données pour en apprendre plus. Ça a aussi comme avantage de nous permettre de juger de la popularité de certains jeux par la quantification des visites, si on le souhaite.

Il n'est pas nécessaire de répéter le `publisher` car il s'agit dans notre cas de Genovalia dans tous les cas. À la limite, l'option de l'afficher pourrait être présente si et seulement si la valeur est différente de Genovalia. Il en va de même pour le `contact_point`, qui est aussi Genovalia dans la majorité des cas.

Il serait peut-être aussi pertinent de limiter l'information sur les licenses et doits d'accès qu'à l'intérieur de la page d'un jeu afin de ne pas décourager les visiteurs. Même chose pour les boutons qui font référence à un schéma ou autre navigation ou information complexe.

Les propriétés suivantes sont proposées:
- titre
- description
- espèce
- mots-clés (sous forme de pillule?)
- publisher (optionnel, si différent de Genovalia)
- date de publication

#### Page d'un jeu de données

La page d'un jeu de données devrait contenir les éléments suivants:
- titre
- description
- identifiant unique
- espèce
- thème(s)
- mots-clés
- auteur(s)
- Point de contact
- droits d'accès
- license
- date de publication
- date de mise à jour

On pourrait y retrouver des metadonnées supplémentaires:
- schéma de variables dynamique
- bouton de contact vers un formulaire de demande d'accès
- fichiers disponibles
- taille de l'échantillon
- relations avec d'autres jeux
- liste de publications qui citent ce jeu de données
- etc.



## Réflexion sur les relations

Une `dcat:Resource` possède une propriété `is_referenced_by` qui peut servir à ajouter des publications qui font référence à celui-ci. Il existe aussi la propriété `resource_relation` qui est plus générique, où la nature de la relation n'est pas spécifiée. Ceci pourrait être utilisé pour relier un jeu de données avec des valeurs temporelles codifiées à une liste de villes ou de lacs, par exemple. Par contre, `qualified_relation` semble plus adapté. Finalement, la propriété `qalified_attribution` semble particulièrement intéressante; elle permet de relier une ressource à un agent par une relation définie par `dcat:Relationship`, ce qui permet de clarifier cette dernière. Un exemple est d'utiliser [CI_RoleCode](https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml) pour définir une relation entre un agent et un jeu de données, comme différencier `author` de `coAuthor`, `editor`, `funder` ou même `stakeholder`.

```yaml
dcat:Relationship:
    relation:
        property: http://purl.org/dc/terms/relation
        range: https://www.w3.org/2000/01/rdf-schema#Resource
        definition: A link to a description of a relationship with another resource.
    had_role:
        property: https://www.w3.org/ns/dcat#hadRole
        range: https://www.w3.org/TR/vocab-dcat-2/#Class:Role
        definition: The function of an entity or agent with respect to another entity or resource. May be used in a qualified-attribution to specify the role of an Agent with respect to an Entity. May be used in a qualified-relation to specify the role of an Entity with respect to another Entity.
        note: Pas certain de comprendre pourquoi le nom de la propriété est au passé; selon les descriptions un rôle actuel est insinué. Utiliser un CI_RoleCode pour représenter le rôle de l'agent, ou un autre vocabulaire pour un rôle d'une autre entité.
```

## Personnes et organisations

DCAT utilise les objects `foaf:Person` et `foaf:Organisation` pour représenter les personnes et les organisations. Ces objets sont utilisés pour représenter les créateurs, les éditeurs, les contacts, etc. Il est recommandé d'utiliser des URIs pour représenter ces entités, afin de faciliter la recherche et la réutilisation des données.

EN COURS DE RÉDACTION

## Réflexion sur le versionnage

EN COURS DE RÉDACTION

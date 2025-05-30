from pyld import jsonld
import json

jsonld.set_document_loader(jsonld.requests_document_loader(timeout=10))

doc = {
    "http://schema.org/name": "Manu Sporny",
    "http://schema.org/url": {"@id": "http://manu.sporny.org/"},
    "http://schema.org/image": {"@id": "http://manu.sporny.org/images/manu.png"},
    "@type": "Person",
}

context = {
    "name": "http://schema.org/name",
    "homepage": {"@id": "http://schema.org/url", "@type": "@id"},
    "image": {"@id": "http://schema.org/image", "@type": "@id"},
    "Person": "http://schema.org/Person",
}

# compact a document according to a particular context
# see: https://json-ld.org/spec/latest/json-ld/#compacted-document-form
compacted = jsonld.compact(
    doc,
    context,
    {
        "graph": True,
    },
)

print(json.dumps(compacted, indent=2))

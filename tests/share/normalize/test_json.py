from share.normalize import *  # noqa


EXAMPLE = {
    "article_id": 3436874,
    "title": "Photochemical Carbon Dioxide Reduction on Mg-Doped\nGa(In)N Nanowire Arrays under Visible Light Irradiation",
    "DOI": "https://dx.doi.org/10.1021/acsenergylett.6b00119.s001",
    "description": "The photochemical reduction of carbon\ndioxide (CO<sub>2</sub>)\ninto energy-rich products can potentially address some of the critical\nchallenges we face today, including energy resource shortages and\ngreenhouse gas emissions. Our ab initio calculations show that CO<sub>2</sub> molecules can be spontaneously activated on the clean nonpolar\nsurfaces of wurtzite metal nitrides, for example, Ga\u00ad(In)\u00adN. We have\nfurther demonstrated the photoreduction of CO<sub>2</sub> into methanol\n(CH<sub>3</sub>OH) with sunlight as the only energy input. A conversion\nrate of CO<sub>2</sub> into CH<sub>3</sub>OH (\u223c0.5 mmol g<sub>cat</sub><sup>\u20131</sup> h<sup>\u20131</sup>) is achieved\nunder visible light illumination (>400 nm). Moreover, we have discovered\nthat the photocatalytic activity for CO<sub>2</sub> reduction can\nbe drastically enhanced by incorporating a small amount of Mg dopant.\nThe definitive role of Mg dopant in Ga\u00ad(In)\u00adN, at both the atomic and\ndevice levels, has been identified. This study reveals the potential\nof III-nitride semiconductor nanostructures in solar-powered reduction\nof CO<sub>2</sub> into hydrocarbon fuels.",
    "type": "paper",
    "url": "https://api.figshare.com/v1/articles/3436874",
    "published_date": "00:00, 08 Jun, 2016",
    "authors": [
        {"author_name": "B. AlOtaibi"},
        {"author_name": "X. Kong"},
        {"author_name": "S. Vanka"},
        {"author_name": "S. Y. Woo"},
        {"author_name": "A. Pofelski"},
        {"author_name": "F. Oudjedi"},
        {"author_name": "S. Fan"},
        {"author_name": "M. G. Kibria"},
        {"author_name": "G. A. Botton"},
        {"author_name": "W. Ji"},
        {"author_name": "H. Guo"},
        {"author_name": "Z. Mi"}
    ],
    "links": [],
    "defined_type": "paper",
    "modified_date": "17:37, 14 Jun, 2016"
}


class Person(Parser):
    given_name = ParseName(ctx.author_name).first
    family_name = ParseName(ctx.author_name).last


class Contributor(Parser):
    person = Delegate(Person, ctx)


class Manuscript(Parser):
    title = ctx.title
    description = ctx.description
    # publish_date = ParseDate(ctx.published_date)
    contributors = Map(Delegate(Contributor, ctx.authors))

    class Extra:
        type = ctx.defined_type
        defined_type = ctx.defined_type


class TestParser:

    def test_parser(self):
        parsed = Manuscript(EXAMPLE).parse()
        assert ctx.pool[parsed]['extra'] == {'type': 'paper', 'defined_type': 'paper'}

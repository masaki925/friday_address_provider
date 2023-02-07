# Address Provider

FRIDAY code challenge: https://gist.github.com/frank-kutzey-friday/76f9bf6b5b8901f7a88cab059fe606c9

## Overview

- Street notation depends on the address of each country/region
- Even in the same country, there are some different notation for same address
  - e.g. `3丁目` == `三丁目`
- So the conversion process could be complex.
- To mitigate the complex, I've divided converters for each country/region, then contained complex logic into each converter.
- I've applied the `Facade pattern` so that the main program can use converters without knowing the complex logics, but just call the `convert()` method and get the `MyData` result.

## How to use

You can run with make commands as below:

```sh
$ cd address_provider
$ make run ADDRESS="Winterallee 3"
poetry run python src/address_provider/main.py --address "Winterallee 3"
{'street': 'Winterallee', 'housenumber': '3'}
```

You can run test as well:

```sh
$ make test
poetry run pytest -v tests
========================================================= test session starts =========================================================
platform darwin -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0 -- ${HOME}/Library/Caches/pypoetry/virtualenvs/address-provider-lv8EGNWZ-py3.11/bin/python
cachedir: .pytest_cache
rootdir: ${HOME}/address_provider
plugins: describe-2.0.1
collected 5 items

tests/test_main.py::test_main[Winterallee 3-expected0] PASSED                                                                   [ 20%]
tests/test_main.py::test_main[Musterstrasse 45-expected1] PASSED                                                                [ 40%]
tests/test_main.py::test_main[Blaufeldweg 123B-expected2] PASSED                                                                [ 60%]
tests/test_main.py::test_main2[Am B\xe4chle 23-expected0] PASSED                                                                [ 80%]
tests/test_main.py::test_main2[Auf der Vogelwiese 23 b-expected1] PASSED                                                        [100%]

========================================================== 5 passed in 0.07s =========================================================
```

## System structure & tools

- `Poetry` to manage the dependencies
- `Pytest` to write a unit test
- `abc` to define Abstract Model to have Polymophic classes
  - By using it, we can ensure that each derivative converter has the same I/F such as `convert()` takes in string to convert, and returns `MyData` as the result.
- `Facade pattern` for `Open Closed` principle.
  - By using it, we can define new converters following a new format of address notation without changing existing converters.

## What I want to have in future

- Creating Detector that can detect which kind of notation is the address, and assign a suitable Converter.
  - We need to take into account the same address but in other country?
  - As far as the requirement, we don't have to. creating the Converter for each languages is one another option.
  - If possible, getting country code as additional information would be nice to have.
- Docker environment
- Define CI/CD process
  - Run the test each CI process.
  - Currently, we only have `test_main.py` but we can separate it into the one for each converter.
- Terraform or other IaC tools to manage the infrastructure

## FYI

ChatGPT couldn't handle japanese address correctly :P


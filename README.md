# API Pets project

This project is to build an automation framework with different programming languages from the following [API Service](https://petstore.swagger.io/)

## Python

### Libraries
- [behave](https://behave.readthedocs.io/en/latest/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [allure-behave](https://pypi.org/project/allure-behave/)

### Installation
To install the the neccesary libraries you can run the following line:
```bash
cd APIPython
pip install -r requirements.txt
```

### Usage
In the framework we have two types of labels **Acceptance** and **Negative**

To execute the whole set of tests
```bash
behave PetsProject/test/features/
```
To ececute the set of tests labeled with **Acceptance**
```bash
behave PetsProject/test/features/ --tags=Acceptance
```
To ececute the set of tests labeled with **Acceptance**
```bash
behave PetsProject/test/features/ --tags=Negative
```
To generate an allure report
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results/ PetsProject/test/features
```

To rise the server to see the report
```bash
allure serve allure-results
```
**_IMPORTANT: IT IS NECCESARY TO HAVE ALLURE INSTALLED_**
### Contributors

The contributors of this project are the following:

[<img src="https://github.com/Hugo96sa.png" width="60px;"/><br/><sub><a href="https://github.com/Hugo96sa">Hugo96sa</a></sub>](https://github.com/MauricioAliendre182/APIPython)

[<img src="https://github.com/sergioale90.png" width="60px;"/><br/><sub><a href="https://github.com/sergioale90">sergioale90</a></sub>](https://github.com/MauricioAliendre182/APIPython)

[<img src="https://github.com/alfregta.png" width="60px;"/><br/><sub><a href="https://github.com/alfregta">alfregta</a></sub>](https://github.com/MauricioAliendre182/APIPython)

[<img src="https://github.com/MauricioAliendre182.png" width="60px;"/><br/><sub><a href="https://github.com/MauricioAliendre182">MauricioAliendre182</a></sub>](https://github.com/MauricioAliendre182/APIPython)

## License

This framework is free and it can be used by anyone
{
  "id": "ee213dd2-8e57-41f5-bdb1-f85d5291e413",
  "version": "2.0",
  "name": "assignment",
  "url": "https://demo.opencart.com/",
  "tests": [{
    "id": "8bb20ed1-60ea-4dda-8db8-03b071bb6629",
    "name": "demo",
    "commands": [{
      "id": "e7da4758-a896-49a1-9642-48c7af88ac56",
      "comment": "",
      "command": "open",
      "target": "https://demo.opencart.com/",
      "targets": [],
      "value": ""
    }, {
      "id": "79b33b02-3204-4d5e-9db7-4a1607ba9170",
      "comment": "",
      "command": "setWindowSize",
      "target": "1550x830",
      "targets": [],
      "value": ""
    }, {
      "id": "863508ec-4646-4b87-9280-dd828cb703dc",
      "comment": "",
      "command": "click",
      "target": "linkText=Desktops",
      "targets": [
        ["linkText=Desktops", "linkText"],
        ["css=.show:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Desktops')]", "xpath:link"],
        ["xpath=//div[@id='narbar-menu']/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'https://demo.opencart.com/en-gb/catalog/desktops')]", "xpath:href"],
        ["xpath=//nav/div[2]/ul/li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Desktops')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "af0db6bf-cdb1-4e8d-bcb3-d0131a60db62",
      "comment": "",
      "command": "click",
      "target": "linkText=Mac (1)",
      "targets": [
        ["linkText=Mac (1)", "linkText"],
        ["css=.show li:nth-child(2) > .nav-link", "css:finder"],
        ["xpath=//a[contains(text(),'Mac (1)')]", "xpath:link"],
        ["xpath=//div[@id='narbar-menu']/ul/li/div/div/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'https://demo.opencart.com/en-gb/catalog/desktops/mac')]", "xpath:href"],
        ["xpath=//div/div/ul/li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Mac (1)')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "5344aa69-17a8-4ad4-814f-f393a750efb6",
      "comment": "",
      "command": "mouseDownAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-193"
    }, {
      "id": "757ea808-4ac0-457c-a404-0708781d950d",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-193"
    }, {
      "id": "53b33b89-34f9-44f4-9184-7534d1bc9b7a",
      "comment": "",
      "command": "mouseUpAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-193"
    }, {
      "id": "8624daf2-206b-456f-b51b-2ee4d14cee4e",
      "comment": "",
      "command": "click",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "60b76276-c75e-448b-b8cb-e7b5fc289a46",
      "comment": "",
      "command": "select",
      "target": "id=input-sort",
      "targets": [],
      "value": "label=Name (A - Z)"
    }, {
      "id": "b0b103cd-a29d-4c05-b4f4-d50a28cd8f17",
      "comment": "",
      "command": "click",
      "target": "css=#input-sort > option:nth-child(2)",
      "targets": [
        ["css=#input-sort > option:nth-child(2)", "css:finder"],
        ["xpath=//option[@value='https://demo.opencart.com/en-gb/catalog/desktops/mac?sort=pd.name&order=ASC']", "xpath:attributes"],
        ["xpath=//select[@id='input-sort']/option[2]", "xpath:idRelative"],
        ["xpath=//option[2]", "xpath:position"],
        ["xpath=//option[contains(.,'Name (A - Z)')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "7a6622f4-9463-4faa-b0d9-8a1f9e44c623",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "606c32e3-db23-4557-bdb6-8c78b4039e4c",
      "comment": "",
      "command": "click",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "df548a08-2dec-40a2-984f-5e9c1b68af90",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d08562b2-c587-4c4f-b887-f8485bfd0ad2",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button-group > button:nth-child(2)",
      "targets": [
        ["css=.button-group > button:nth-child(2)", "css:finder"],
        ["xpath=(//button[@type='submit'])[3]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button[2]", "xpath:idRelative"],
        ["xpath=//form/div/button[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "84ec150f-c422-417a-9f89-38fd7a2c5611",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button-group > button:nth-child(2)",
      "targets": [
        ["css=.button-group > button:nth-child(2)", "css:finder"],
        ["xpath=(//button[@type='submit'])[3]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button[2]", "xpath:idRelative"],
        ["xpath=//form/div/button[2]", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "649184ec-c0f3-44c1-91e7-2ea185b2d780",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": []
  }],
  "urls": [],
  "plugins": []
}
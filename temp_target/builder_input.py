project_structure = {
    "product": "VacationHouse",
    "types": ["OceanBeach", "RockMountain"],
    "parts": ["FoundationBase", "InteriorDesign"],
    "parent_steps": ["prepare_the_foundation", "inspect_foundation"],
    "child_steps": ["build_the_structure", "finalize_details"]
}






project/
│
├── builders/
│   ├── abstract_builder/
│   │   └── vacation_house_builder.py
│   ├── ocean_beach_vacation_house_builder.py
│   └── rock_mountain_vacation_house_builder.py
│
├── product/
│   └── vacation_house.py
│
├── parts/
│   ├── foundation_base.py
│   ├── interior_design.py
│
├── director/
│   └── director.py
│
└── tests/
    ├── test_ocean_beach_vacation_house.py
    └── test_rock_mountain_vacation_house.py

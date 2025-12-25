
class Project:
    """
    manage the imported datasets in current project. 
    the datasets in one project will be shown in the same plot. 
    """

    def __init__(self) -> None:
        self._initialize = False

        self.data_type = ""
        self.x_type = ""
        self.y_type = ""

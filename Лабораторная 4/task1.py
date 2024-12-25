class SocialNetwork:
    """
    Base class representing a social network.
    """

    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        return f"SocialNetwork(name={self.name}, users={self.users})"

    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name!r}, users={self.users!r})"

    def get_user_count(self) -> int:
        """
        Returns the number of users in the social network.
        """
        return self.users


class VK(SocialNetwork):
    """
    Derived class representing VK social network.
    """

    def __init__(self, name: str, users: int, groups: int):
        super().__init__(name, users)
        self.groups = groups

    def __str__(self) -> str:
        return f"VK(name={self.name}, users={self.users}, groups={self.groups})"

    def __repr__(self) -> str:
        return f"VK(name={self.name!r}, users={self.users!r}, groups={self.groups!r})"

    def get_user_count(self) -> int:
        """
        Overridden method to return the number of users in VK.
        This method is overridden to demonstrate how the
        user count might be calculated differently for VK.
        """
        return self.users + self.groups  # Example logic: users + groups

    def get_group_count(self) -> int:
        """
        Returns the number of groups in VK.
        """
        return self.groups


if __name__ == """__main__""":
    pass

from .application import ApplicationContainer
from .core import Core
from .domain import DomainContainer

di_container = Core()
service_container = DomainContainer()
application_container = ApplicationContainer(
    dice_service=service_container.dice_service(),
)

__all__ = ["application_container", "di_container"]

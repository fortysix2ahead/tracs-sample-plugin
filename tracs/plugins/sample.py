from logging import getLogger
from typing import Any, Iterable, List, Optional, Tuple, Union

from tracs.activity import Activity
from tracs.config import ApplicationContext
from tracs.registry import service
from tracs.resources import Resource
from tracs.service import Service

log = getLogger( __name__ )

# sample plugin

SERVICE_NAME = 'sample'
DISPLAY_NAME = 'Sample Service'

class SampleActivity( Activity ):
	pass

@service
class Sample( Service ):

	def __init__( self, **kwargs ):
		super().__init__( name=SERVICE_NAME, display_name=DISPLAY_NAME, **kwargs )

	def url_for_id( self, local_id: Union[int, str] ) -> Optional[str]:
		return None

	def url_for_resource_type( self, local_id: Union[int, str], type: str ) -> Optional[str]:
		return None

	def login( self ) -> bool:
		return True

	def fetch( self, force: bool = False, **kwargs ) -> Iterable[Activity]:
		return []

	def download( self, summary: Resource, force: bool = False, pretend: bool = False, **kwargs ) -> List[Resource]:
		return []

	def download_resource( self, resource: Resource, **kwargs ) -> Tuple[Any, int]:
		return [], 200

	def setup( self, ctx: ApplicationContext ) -> None:
		pass

	# noinspection PyMethodMayBeStatic
	def setup_complete( self ) -> bool:
		return True

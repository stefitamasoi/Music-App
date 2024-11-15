from service.statisticsservice import StatisticsService
from service.songservice import SongService
from service.listenerservice import ListenerService
from repository.repository import Repository
from ui.console import UI

song_repository = Repository()
listener_repository = Repository()

song_service = SongService(song_repository)
listener_service = ListenerService(listener_repository)
statistics_service = StatisticsService(song_repository, listener_repository)

console = UI(song_service, listener_service, statistics_service)
console.run()

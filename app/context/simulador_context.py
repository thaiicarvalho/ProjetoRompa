from app.states.postura_ativa_state import (
    PosturaAtivaState
)

from app.states.postura_reflexiva_state import (
    PosturaReflexivaState
)

from app.states.postura_omissa_state import (
    PosturaOmissaState
)


class SimuladorContext:

    def __init__(self, percentual):

        self.percentual = percentual

        self.state = self.definir_state()

    def definir_state(self):

        if self.percentual >= 70:

            return PosturaAtivaState()

        elif self.percentual >= 40:

            return PosturaReflexivaState()

        return PosturaOmissaState()

    def gerar_resultado(self):

        resultado = self.state.gerar_resultado()

        resultado["percentual"] = self.percentual

        return resultado
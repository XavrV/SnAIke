
# 🐍 Snake IA - Progreso de Desarrollo (README_PROGRESO1.md)

## 🎯 Enfoque y Contexto del Proyecto

- **Tipo de proyecto:** Formativo, basado en aprendizaje por proyectos (PBL).
- **Objetivo principal:** Aprender y aplicar conceptos clave de *Machine Learning* profesional en un entorno lúdico y visual: el juego Snake.
- **Stack actual:**
  - Lenguaje: `Python 3.12`
  - Editor: `Visual Studio Code`
  - Asistente: `GitHub Copilot`
  - Framework visual: `pygame`
  - Control de versiones: `git + GitHub`

---

## 🧱 Estructura del Proyecto

```
snake-ia/
├── src/                        # Código fuente organizado por módulos
│   ├── game/                  # Lógica del juego Snake
│   ├── state/                 # Representación del estado para la IA
│   └── ...                   # Futuras carpetas: rl/, supervised/, evaluation/
├── tests/                     # Tests automáticos
├── notebooks/                 # Exploraciones interactivas (Jupyter)
├── data/                      # Datasets y resultados
├── visualizar_estado.py       # Script visual para depuración del estado
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧩 Módulos Implementados y Funcionando

### 1. `SnakeGame` (`src/game/snake_game.py`)
- Lógica central del juego:
  - Movimiento de la serpiente.
  - Detección de colisiones.
  - Generación aleatoria de comida.
  - Método `play_step(action)` listo para integrar con agentes.
- Visualización:
  - `render_console()`: modo texto.
  - ✅ `render_pygame()`: visualización en ventana con `pygame`.

### 2. Test Inicial (`tests/test_game.py`)
- Script de prueba funcional con acciones aleatorias.
- Verifica paso a paso que el juego responde correctamente.

### 3. Representación del Estado (`src/state/state_representation.py`)
- Función `get_state(game)` que devuelve un vector binario (11 dimensiones):
  - Peligros (frente, derecha, izquierda)
  - Dirección actual
  - Posición relativa de la comida
- Listo para alimentar modelos de RL.

### 4. Visualizador de Estado (`visualizar_estado.py`)
- Script que:
  - Visualiza en tiempo real el tablero (pygame)
  - Imprime el vector de estado, reward y score
  - Reinicia el juego si hay colisión
- Permite entender cómo percibe el entorno la IA.

---

## 📂 Gestión del Proyecto

- Repositorio inicializado con Git.
- `.gitignore` configurado para entorno Python y archivos auxiliares.
- Pruebas exitosas de cada componente hasta ahora.

---

## 🔜 Siguientes pasos sugeridos (Etapa 3 - RL)

- Crear módulo `rl/` con:
  - `LinearQNet`: red neuronal para Q-Learning.
  - `ReplayMemory`: buffer de experiencia.
  - `QTrainer`: entrenamiento RL.
- Iniciar aprendizaje básico.

---


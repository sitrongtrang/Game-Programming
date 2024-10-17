# # Compiler
# CXX = g++

# # Output binary name
# TARGET = tiny_football

# # Source files for tiny_football and ImGui
# SRC = tiny_football.cpp
# IMGUI_DIR = ./imgui
# IMGUI_SRC = $(IMGUI_DIR)/imgui.cpp $(IMGUI_DIR)/imgui_demo.cpp $(IMGUI_DIR)/imgui_draw.cpp $(IMGUI_DIR)/imgui_tables.cpp $(IMGUI_DIR)/imgui_widgets.cpp
# IMGUI_BACKEND = $(IMGUI_DIR)/backends/imgui_impl_sdl2.cpp $(IMGUI_DIR)/backends/imgui_impl_opengl3.cpp

# # Combine all source files
# ALL_SRC = $(SRC) $(IMGUI_SRC) $(IMGUI_BACKEND)

# # Compiler flags
# CXXFLAGS = -std=c++11 -I$(IMGUI_DIR) -I$(IMGUI_DIR)/backends -g -Wall -Wformat

# # Platform detection
# UNAME_S := $(shell uname -s)

# # Platform-specific configurations
# ifeq ($(UNAME_S), Linux) # LINUX
#     ECHO_MESSAGE = "Building for Linux"
#     LIBS = -lGL -ldl `sdl2-config --libs`
#     CXXFLAGS += `sdl2-config --cflags`
# endif

# ifeq ($(UNAME_S), Darwin) # MACOS
#     ECHO_MESSAGE = "Building for macOS"
#     LIBS = -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo `sdl2-config --libs`
#     CXXFLAGS += `sdl2-config --cflags` -I/usr/local/include -I/opt/local/include
# endif

# ifeq ($(OS), Windows_NT) # WINDOWS (MinGW)
#     ECHO_MESSAGE = "Building for Windows (MinGW)"
#     LIBS = -lgdi32 -lopengl32 -limm32 `pkg-config --static --libs sdl2`
#     CXXFLAGS += `pkg-config --cflags sdl2`
# endif

# # Build rules
# all: $(TARGET)
# 	@echo $(ECHO_MESSAGE)

# $(TARGET): $(ALL_SRC)
# 	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

# # Clean up build files
# clean:
# 	rm -f $(TARGET)

# # Phony targets
# .PHONY: all clean



# Compiler
CXX = g++

# Output binary name
TARGET = tiny_football

# Source files for tiny_football, keySetMenu, keyBinding, and ImGui
SRC = tiny_football.cpp ./src/utils.cpp ./src/keySetMenu.cpp ./src/keyBinding.cpp ./src/Physics.cpp ./src/Ball.cpp ./src/Footballer.cpp ./src/Surface.cpp ./src/Wind.cpp
MENU_SRC = $(wildcard ./src/menu/*.cpp) ./src/Constant.cpp
IMGUI_DIR = ./imgui
IMGUI_SRC = $(IMGUI_DIR)/imgui.cpp $(IMGUI_DIR)/imgui_demo.cpp $(IMGUI_DIR)/imgui_draw.cpp $(IMGUI_DIR)/imgui_tables.cpp $(IMGUI_DIR)/imgui_widgets.cpp
IMGUI_BACKEND = $(IMGUI_DIR)/backends/imgui_impl_sdl2.cpp $(IMGUI_DIR)/backends/imgui_impl_opengl3.cpp

# Combine all source files
ALL_SRC = $(SRC) $(IMGUI_SRC) $(IMGUI_BACKEND) $(MENU_SRC)

# Object files
OBJS = tiny_football.o ./src/utils.o ./src/keySetMenu.o ./src/keyBinding.o ./src/Physics.o ./src/Ball.o ./src/Footballer.o ./src/Surface.o ./src/Wind.o $(IMGUI_SRC:.cpp=.o) $(IMGUI_BACKEND:.cpp=.o) $(MENU_SRC:.cpp=.o)

# Compiler flags
CXXFLAGS = -std=c++11 -I$(IMGUI_DIR) -I$(IMGUI_DIR)/backends -I./headers -g -Wall -Wformat  # Include headers path

# Platform detection
UNAME_S := $(shell uname -s)

# Platform-specific configurations
ifeq ($(UNAME_S), Linux) # LINUX
    ECHO_MESSAGE = "Building for Linux"
    LIBS = -lGL -ldl `sdl2-config --libs`
    CXXFLAGS += `sdl2-config --cflags`
endif

ifeq ($(UNAME_S), Darwin) # MACOS
    ECHO_MESSAGE = "Building for macOS"
    LIBS = -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo `sdl2-config --libs`
    CXXFLAGS += `sdl2-config --cflags` -I/usr/local/include -I/opt/local/include
endif

ifeq ($(OS), Windows_NT) # WINDOWS (MinGW)
    ECHO_MESSAGE = "Building for Windows (MinGW)"
    LIBS = -lgdi32 -lopengl32 -limm32 `pkg-config --static --libs sdl2 sdl2_image`
    CXXFLAGS += `pkg-config --cflags sdl2`
endif

# Build rules
all: $(TARGET)
	@echo $(ECHO_MESSAGE)

$(TARGET): $(OBJS)
	$(CXX) -o $@ $^ $(CXXFLAGS) $(LIBS)

# Generic pattern rule to compile .cpp files into .o files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Specific rules for ImGui source files
$(IMGUI_DIR)/%.o: $(IMGUI_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(IMGUI_DIR)/backends/%.o: $(IMGUI_DIR)/backends/%.cpp
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Clean up build files
clean:
	rm -f $(TARGET) $(OBJS)

# Phony targets
.PHONY: all clean
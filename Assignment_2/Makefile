# Compiler
CXX = g++

# Output binary name
TARGET = tiny_football

# Source files for tiny_football and ImGui
SRC = tiny_football.cpp
IMGUI_DIR = ./imgui
IMGUI_SRC = $(IMGUI_DIR)/imgui.cpp $(IMGUI_DIR)/imgui_demo.cpp $(IMGUI_DIR)/imgui_draw.cpp $(IMGUI_DIR)/imgui_tables.cpp $(IMGUI_DIR)/imgui_widgets.cpp
IMGUI_BACKEND = $(IMGUI_DIR)/backends/imgui_impl_sdl2.cpp $(IMGUI_DIR)/backends/imgui_impl_opengl3.cpp

# Combine all source files
ALL_SRC = $(SRC) $(IMGUI_SRC) $(IMGUI_BACKEND)

# Compiler flags
CXXFLAGS = -std=c++11 -I$(IMGUI_DIR) -I$(IMGUI_DIR)/backends -g -Wall -Wformat

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
    LIBS = -lgdi32 -lopengl32 -limm32 `pkg-config --static --libs sdl2`
    CXXFLAGS += `pkg-config --cflags sdl2`
endif

# Build rules
all: $(TARGET)
	@echo $(ECHO_MESSAGE)

$(TARGET): $(ALL_SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

# Clean up build files
clean:
	rm -f $(TARGET)

# Phony targets
.PHONY: all clean

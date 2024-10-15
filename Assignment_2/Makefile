# Compiler
CXX = g++

# Source files for tiny_football and ImGui
SRC = tiny_football.cpp
IMGUI_DIR = ./imgui
IMGUI_SRC = $(IMGUI_DIR)/imgui.cpp $(IMGUI_DIR)/imgui_demo.cpp $(IMGUI_DIR)/imgui_draw.cpp $(IMGUI_DIR)/imgui_tables.cpp $(IMGUI_DIR)/imgui_widgets.cpp
IMGUI_BACKEND = $(IMGUI_DIR)/backends/imgui_impl_sdl2.cpp $(IMGUI_DIR)/backends/imgui_impl_opengl3.cpp

# Combine all source files
ALL_SRC = $(SRC) $(IMGUI_SRC) $(IMGUI_BACKEND)

# Output binary name
TARGET = tiny_football

# Compiler and linker flags
CXXFLAGS = -Wall -Wextra -g -std=c++11 -I/usr/include/SDL2 -I$(IMGUI_DIR) -I$(IMGUI_DIR)/backends
LDFLAGS = -lSDL2 -lGL -lGLU -ldl

# Default target
all: $(TARGET)

# Rule to create the target executable
$(TARGET): $(ALL_SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

# Target to run the program
run: $(TARGET)
	./$(TARGET)

# Clean up build files
clean:
	rm -f $(TARGET)

# Phony targets
.PHONY: all clean run

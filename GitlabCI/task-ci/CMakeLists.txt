cmake_minimum_required(VERSION 3.5)

# Настройки RPATH
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")

project(TaskCI)

# Настройки выходных директорий
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Подключение зависимостей
add_subdirectory(3rdparty/googletest)

# Подключение модулей проекта
add_subdirectory(B)
add_subdirectory(C)

# Включение системы тестирования
enable_testing()

# Установка компонентов
install(
    TARGETS C ClassLib CTestExe
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

# Установка заголовочных файлов (если есть)
install(
    DIRECTORY ${CMAKE_SOURCE_DIR}/B/
    DESTINATION include
    FILES_MATCHING PATTERN "*.h"
)

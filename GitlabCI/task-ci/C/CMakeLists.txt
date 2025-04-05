# Основное приложение
add_executable(C main.cpp)
target_link_libraries(C PRIVATE ClassLib)
target_include_directories(C PRIVATE ${CMAKE_SOURCE_DIR})

# Тестовый исполняемый файл
add_executable(CTestExe main_test.cpp tests.cpp)
target_link_libraries(CTestExe 
    PRIVATE 
    gtest_main 
    ClassLib
)
target_include_directories(CTestExe PRIVATE ${CMAKE_SOURCE_DIR})

# Регистрация тестов
include(GoogleTest)
gtest_discover_tests(CTestExe
    EXTRA_ARGS "--gtest_output=xml:${CMAKE_BINARY_DIR}/test_results/test_results.xml"
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    DISCOVERY_TIMEOUT 60
)

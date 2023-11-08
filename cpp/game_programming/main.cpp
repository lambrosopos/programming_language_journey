void GameEngine::mainLoop() {
    m_entityManager.update();
    sUserInput();
    sMovement();
    sCollision();
    sRender();
    m_currentFrame++;
}

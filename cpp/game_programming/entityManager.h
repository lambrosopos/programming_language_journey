class Entity {
    const size_t        m_id    = 0;
    const std::string   m_tag   = "Default";
    bool                m_alive = true;
public:
    std::shared_ptr<CTransform> cTransform;
    std::shared_ptr<CName> cName;
    std::shared_ptr<CShape> cShape;
    std::shared_ptr<CBBox> cBBox;
    Entity(const std::string& tag, size_t id);

    void destroy() { 
        m_alive = false;
    }

    const std::string& tag() {
        return m_tag;
    }

typedef std::vector<std::shared_ptr<Entity>>    EntityVec;
typedef std::map<std::string, EntityVec>        EntityMap;

class EntityManager {
    EntityVec m_entities;
    EntityVec m_toAdd;
    EntityMap m_entityMap;
    size_t m_totalEntities = 0;
public:
    EntityManager();

    void update() {
        // Solve iterator invalidation logic here only
        for (auto e : m_toAdd) {
            m_entities.push_back(e);
            m_entityMap[e->tag()].push_back(e);
        }

        for (auto e: m_entities) {
        }

        m_toAdd.clear();
    }

    std::shared_ptr<Entity> addEntity(const std::string& tag) {
        auto e = std::make_shared<Entity>(tag, m_totalEntities++);
        m_toAdd.push_back(e); // Leave the adding of the entity for next loop
        return e;
    }

    EntityVec& getEntities();
    EntityVec& getEntities(const std::string& tag);
};


// Usage Example
EntityManager m_entities;
void spawnEnemy()
    auto e = m_entities.addEntity("enemy");
    e->cTransform = std:make_shared<CTransform>(args);
    e->cShape = std:make_shared<CShape>(args);

void collisions() {
    for (auto b : m_entities.getEntities("bullet")) {
        for (auto e : m_entities.getEntities("enemy")) {
            if (Physics::CheckCollision(b, e)) {
                b->destroy(); e->destroy();
            }
    }
}


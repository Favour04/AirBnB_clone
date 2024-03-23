const { v4: uuidv4 } = require('uuid');

class BaseModel {
    constructor() {
        this.id = uuidv4();
        this.created_at = new Date();
        this.updated_at = this.created_at;
    }

    toString() {
        return `[${this.constructor.name}] (${this.id}) ${JSON.stringify(this)}`;
    }

    save() {
        this.updated_at = new Date().toISOString();
    }

    toDict() {
        let dict = { ...this, __class__: this.constructor.name };
        dict["created_at"] = this.created_at.toISOString();
        dict["updated_at"] = this.updated_at.toISOString();
        return dict;
    }
}
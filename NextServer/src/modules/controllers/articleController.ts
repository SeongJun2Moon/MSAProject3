import { Article } from "@/src/modules/types";
import { author } from "@/src/modules/controllers";

export class ArticleController {
    async write(writtenData: Article) : Promise<any> {
        try {
            await author.post('/Article', writtenData)
        } catch (error) {
            return error;
        }
    }

}
import createPushNotificationsJobs from "./8-job";
import { expect } from "chai";
import kue from 'kue';

const queue = kue.createQueue();


const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];


const lists = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];



describe('creatPushNotificationsJobs', () => {
    before(function() {
        queue.testMode.enter();
    });
      
    afterEach(function() {
        queue.testMode.clear();
    });
      
    after(function() {
        queue.testMode.exit()
    });

    it('add job to the queue', function() {
        queue.createJob('myJob', { foo: 'bar' }).save();
        queue.createJob('anotherJob', { baz: 'bip' }).save();
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('myJob');
        expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
    });      

    it('it works if the given is array of of one job object', () => {
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(1);
    })

    it('it works if the given is array of many job object', () => {
        createPushNotificationsJobs(lists, queue);
        expect(queue.testMode.jobs.length).to.equal(4);
    })
    it('it raises type error when using the string', () => {
        expect(() => {
            createPushNotificationsJobs('list', queue);
        }).to.throw('Jobs is not an array');
    })
    it('it raises type error when using the object', () => {
        expect(() => {
            createPushNotificationsJobs({name: "someone", phoneNumber: 1231234}, queue);
        }).to.throw('Jobs is not an array');
    })
    it('it raises type error when using the Number', () => {
        expect(() => {
            createPushNotificationsJobs(1237, queue);
        }).to.throw('Jobs is not an array');
    })
})